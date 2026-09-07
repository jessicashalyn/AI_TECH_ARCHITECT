import json
from django.conf import settings
from google import genai
# pyrefly: ignore [missing-import]
from google.genai import types
from .schemas import ArchitectureResponse
from .prompts import SYSTEM_PROMPT
import logging

logger = logging.getLogger(__name__)

def generate_architecture_from_requirements(requirements_data: dict) -> dict:
    if not settings.AI_API_KEY:
        logger.error("AI_API_KEY is not configured in settings")
        raise ValueError("AI_API_KEY is not configured")
        
    logger.info(f"Using AI_MODEL: {settings.AI_MODEL}")
    logger.info(f"AI_API_KEY length: {len(settings.AI_API_KEY)}")
    
    try:
        client = genai.Client(api_key=settings.AI_API_KEY)
    except Exception as e:
        logger.error("Failed to initialize genai.Client", exc_info=True)
        raise
    
    prompt = f"Project Requirements:\n{json.dumps(requirements_data, indent=2)}\n\nGenerate the optimal architecture."
    
    try:
        response = client.models.generate_content(
            model=settings.AI_MODEL,
            contents=[SYSTEM_PROMPT, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ArchitectureResponse,
                temperature=0.7,
            ),
        )
        
        result_json = response.text
        logger.info(f"AI Response raw length: {len(result_json)}")
        logger.info(f"AI Response raw text starts with: {result_json[:200]}...")
        # the response might have markdown block
        if result_json.startswith("```json"):
            result_json = result_json[7:-3]
            
        validated_data = ArchitectureResponse.model_validate_json(result_json)
        dumped = validated_data.model_dump()
        logger.info(f"Dumped JSON keys: {list(dumped.keys())}")
        
        # Clean mermaid formatting if the AI still included it
        diagram = dumped.get("diagram_data", "")
        if diagram.startswith("```mermaid"):
            diagram = diagram.replace("```mermaid", "").replace("```", "").strip()
        elif diagram.startswith("```"):
            diagram = diagram.replace("```", "").strip()
        dumped["diagram_data"] = diagram
        
        return dumped
    except Exception as e:
        raise Exception(f"AI Generation Failed: {str(e)}")
