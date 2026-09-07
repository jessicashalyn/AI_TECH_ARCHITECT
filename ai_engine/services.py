import json
from django.conf import settings
from google import genai
# pyrefly: ignore [missing-import]
from google.genai import types
from .schemas import ArchitectureResponse
from .prompts import SYSTEM_PROMPT

def generate_architecture_from_requirements(requirements_data: dict) -> dict:
    if not settings.AI_API_KEY:
        raise ValueError("AI_API_KEY is not configured")
        
    client = genai.Client(api_key=settings.AI_API_KEY)
    
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
        # the response might have markdown block
        if result_json.startswith("```json"):
            result_json = result_json[7:-3]
            
        validated_data = ArchitectureResponse.model_validate_json(result_json)
        dumped = validated_data.model_dump()
        
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
