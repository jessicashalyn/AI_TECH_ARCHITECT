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


def generate_architecture_from_requirements(requirements_data: dict) -> dict:

    if not settings.AI_API_KEY:
        logger.error("AI_API_KEY is not configured in settings")
        raise ValueError("AI_API_KEY is not configured")

    logger.info(f"Using AI_MODEL: {settings.AI_MODEL}")

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

    prompt = (
        f"Project Requirements:\n"
        f"{json.dumps(requirements_data, indent=2)}\n\n"
        f"Generate the optimal architecture."
    )

    # Primary model + fallback models
    models = [
        settings.AI_MODEL,
        "gemini-3.5-flash",
        "gemini-3.5-flash-lite",
    ]

    # Remove duplicate model names
    models = list(dict.fromkeys(models))

    last_error = None

    for model in models:

        logger.info(f"Trying Gemini model: {model}")

        # Retry each model up to 3 times
        for attempt in range(3):

            try:

                logger.info(
                    f"Gemini request - model={model}, attempt={attempt + 1}/3"
                )

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

                result_json = response.text

                if not result_json:
                    raise ValueError(
                        "Gemini returned an empty response"
                    )

                logger.info(
                    f"AI Response raw length: {len(result_json)}"
                )

                logger.info(
                    f"AI Response raw text starts with: "
                    f"{result_json[:200]}..."
                )

                # Remove markdown JSON wrapper if present
                result_json = result_json.strip()

                if result_json.startswith("```json"):
                    result_json = result_json[7:]

                if result_json.endswith("```"):
                    result_json = result_json[:-3]

                result_json = result_json.strip()

                validated_data = (
                    ArchitectureResponse.model_validate_json(
                        result_json
                    )
                )

                dumped = validated_data.model_dump()

                logger.info(
                    f"Dumped JSON keys: {list(dumped.keys())}"
                )

                # Clean Mermaid formatting
                diagram = dumped.get("diagram_data", "")

                if diagram.startswith("```mermaid"):
                    diagram = (
                        diagram
                        .replace("```mermaid", "")
                        .replace("```", "")
                        .strip()
                    )

                elif diagram.startswith("```"):
                    diagram = (
                        diagram
                        .replace("```", "")
                        .strip()
                    )

                dumped["diagram_data"] = diagram

                logger.info(
                    f"Architecture generated successfully "
                    f"using model: {model}"
                )

                return dumped

            except ServerError as e:

                last_error = e

                error_text = str(e)

                logger.warning(
                    f"Gemini ServerError with model {model}: "
                    f"{error_text}"
                )

                # Retry only temporary server/unavailable errors
                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                ):

                    if attempt < 2:
                        wait_time = 2 ** attempt

                        logger.info(
                            f"Gemini temporarily unavailable. "
                            f"Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)
                        continue

                    logger.warning(
                        f"Model {model} failed after 3 attempts. "
                        f"Trying fallback model..."
                    )

                    break

                # Other server errors should not blindly retry
                raise

            except Exception as e:

                last_error = e

                logger.error(
                    f"AI generation failed with model {model}: "
                    f"{str(e)}",
                    exc_info=True
                )

                # Validation / JSON / other errors
                # should not switch models unnecessarily
                raise

    # All models failed
    logger.error(
        "All Gemini models failed. Last error: %s",
        str(last_error)
    )

    raise Exception(
        "AI service is temporarily unavailable. "
        "Please try again in a few moments."
    )