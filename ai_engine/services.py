import json
import time
import logging

from django.conf import settings

from google import genai
from google.genai import types
from google.genai.errors import ServerError

from .schemas import ArchitectureResponse, get_gemini_schema
from .prompts import SYSTEM_PROMPT


logger = logging.getLogger(__name__)


def generate_architecture_from_requirements(
    requirements_data: dict
) -> dict:

    # ---------------------------------------------------------
    # 1. Check API Key
    # ---------------------------------------------------------
    if not settings.AI_API_KEY:
        logger.error(
            "AI_API_KEY is not configured in settings"
        )
        raise ValueError(
            "AI_API_KEY is not configured"
        )

    logger.info(
        f"Using AI_MODEL: {settings.AI_MODEL}"
    )

    # ---------------------------------------------------------
    # 2. Initialize Gemini Client
    # ---------------------------------------------------------
    try:
        client = genai.Client(
            api_key=settings.AI_API_KEY
        )

    except Exception:
        logger.error(
            "Failed to initialize genai.Client",
            exc_info=True
        )
        raise

    # ---------------------------------------------------------
    # 3. Build Project Prompt
    # ---------------------------------------------------------
    prompt = (
        f"Project Requirements:\n"
        f"{json.dumps(requirements_data, indent=2)}\n\n"
        f"Generate the optimal architecture."
    )

    # ---------------------------------------------------------
    # 4. Gemini Models
    #
    # Primary model comes from Render environment variable:
    #
    # AI_MODEL=gemini-3.6-flash
    #
    # If it temporarily fails with 503,
    # fallback models will be tried.
    # ---------------------------------------------------------
    models = [
        settings.AI_MODEL,
        "gemini-3.5-flash",
        "gemini-3.5-flash-lite",
    ]

    # Remove duplicate model names
    models = list(dict.fromkeys(models))

    last_error = None

    # ---------------------------------------------------------
    # 5. Try Each Model
    # ---------------------------------------------------------
    for model in models:

        logger.info(
            f"Trying Gemini model: {model}"
        )

        # -----------------------------------------------------
        # Retry each model 3 times
        # -----------------------------------------------------
        for attempt in range(3):

            try:

                logger.info(
                    f"Gemini request - "
                    f"model={model}, "
                    f"attempt={attempt + 1}/3"
                )

                # -------------------------------------------------
                # 6. Generate Gemini Response
                # -------------------------------------------------
                response = client.models.generate_content(

                    model=model,

                    contents=[
                        SYSTEM_PROMPT,
                        prompt
                    ],

                    config=types.GenerateContentConfig(

                        response_mime_type="application/json",

                        response_schema=get_gemini_schema(),

                        temperature=0.7,
                    ),
                )

                # -------------------------------------------------
                # 7. Get Response Text
                # -------------------------------------------------
                result_json = response.text

                if not result_json:
                    raise ValueError(
                        "Gemini returned an empty response"
                    )

                logger.info(
                    f"AI Response raw length: "
                    f"{len(result_json)}"
                )

                logger.info(
                    f"AI Response raw text starts with: "
                    f"{result_json[:200]}..."
                )

                # -------------------------------------------------
                # 8. Clean JSON Markdown Code Fence
                # -------------------------------------------------
                result_json = result_json.strip()

                if result_json.startswith("```json"):
                    result_json = result_json[
                        len("```json"):
                    ].strip()

                elif result_json.startswith("```"):
                    result_json = result_json[
                        len("```"):
                    ].strip()

                if result_json.endswith("```"):
                    result_json = result_json[
                        :-len("```")
                    ].strip()

                # -------------------------------------------------
                # 9. Validate AI Response Against Pydantic Schema
                # -------------------------------------------------
                validated_data = (
                    ArchitectureResponse.model_validate_json(
                        result_json
                    )
                )

                # -------------------------------------------------
                # 10. Convert to Dictionary
                # -------------------------------------------------
                dumped = validated_data.model_dump()

                logger.info(
                    f"Dumped JSON keys: "
                    f"{list(dumped.keys())}"
                )

                # -------------------------------------------------
                # 11. Clean Mermaid Diagram
                # -------------------------------------------------
                diagram = dumped.get(
                    "diagram_data",
                    ""
                )

                if diagram:

                    diagram = diagram.strip()

                    # Remove ```mermaid
                    if diagram.startswith(
                        "```mermaid"
                    ):
                        diagram = diagram[
                            len("```mermaid"):
                        ].strip()

                    # Remove generic ```
                    elif diagram.startswith(
                        "```"
                    ):
                        diagram = diagram[
                            len("```"):
                        ].strip()

                    # Remove closing ```
                    if diagram.endswith(
                        "```"
                    ):
                        diagram = diagram[
                            :-len("```")
                        ].strip()

                    # Convert graph TD → flowchart TD
                    if diagram.startswith(
                        "graph TD"
                    ):
                        diagram = diagram.replace(
                            "graph TD",
                            "flowchart TD",
                            1
                        )

                    # Remove unnecessary whitespace
                    diagram = diagram.strip()

                dumped["diagram_data"] = diagram

                # -------------------------------------------------
                # 12. Success
                # -------------------------------------------------
                logger.info(
                    f"Architecture generated successfully "
                    f"using model: {model}"
                )

                return dumped

            # -----------------------------------------------------
            # 13. Gemini Server Error
            # -----------------------------------------------------
            except ServerError as e:

                last_error = e

                error_text = str(e)

                logger.warning(
                    f"Gemini ServerError with model "
                    f"{model}: {error_text}"
                )

                # -------------------------------------------------
                # Retry temporary 503 / UNAVAILABLE errors
                # -------------------------------------------------
                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                ):

                    if attempt < 2:

                        # 1 second → 2 seconds
                        wait_time = 2 ** attempt

                        logger.warning(
                            f"Gemini temporarily unavailable. "
                            f"Retrying in "
                            f"{wait_time} seconds..."
                        )

                        time.sleep(
                            wait_time
                        )

                        continue

                    # -------------------------------------------------
                    # All 3 attempts failed
                    # Move to next model
                    # -------------------------------------------------
                    logger.warning(
                        f"Model {model} failed after "
                        f"3 attempts. "
                        f"Trying fallback model..."
                    )

                    break

                # Other ServerError
                raise

            # -----------------------------------------------------
            # 14. Other Errors
            # -----------------------------------------------------
            except Exception as e:

                last_error = e

                logger.error(
                    f"AI generation failed with "
                    f"model {model}: {str(e)}",
                    exc_info=True
                )

                # Do not blindly retry validation,
                # JSON, schema or programming errors.
                raise

    # ---------------------------------------------------------
    # 15. All Models Failed
    # ---------------------------------------------------------
    logger.error(
        "All Gemini models failed. "
        f"Last error: {last_error}"
    )

    raise Exception(
        "AI service is temporarily unavailable. "
        "Please try again in a few moments."
    )