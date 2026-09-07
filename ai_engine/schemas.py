from pydantic import BaseModel, Field
from typing import List, Optional
import json

class TechnologyOption(BaseModel):
    name: str
    description: str
    rationale: str

class DatabaseDesign(BaseModel):
    primary_database: str
    caching_layer: Optional[str]
    description: str
    key_tables_collections: List[str]

class ApiArchitecture(BaseModel):
    style: str
    authentication: str
    description: str
    endpoints_summary: List[str]

class CloudArchitecture(BaseModel):
    provider: str
    compute: str
    storage: str
    description: str

class SecurityItem(BaseModel):
    category: str
    recommendations: List[str]

class ArchitectureResponse(BaseModel):
    technology_stack: List[TechnologyOption]
    database_design: DatabaseDesign
    api_architecture: ApiArchitecture
    cloud_architecture: CloudArchitecture
    security_checklist: List[SecurityItem]
    scalability_strategy: List[str]
    diagram_data: str = Field(description="Mermaid.js diagram syntax")
    architecture_score: int = Field(ge=0, le=100)
    strengths: List[str]
    risks: List[str]
    improvements: List[str]
    summary: str

def sanitize_for_gemini(schema, defs):
    ALLOWED_KEYS = {'type', 'properties', 'required', 'items', 'enum', 'description', 'nullable'}
    
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_path = schema["$ref"]
            def_name = ref_path.split("/")[-1]
            resolved = defs.get(def_name, {}).copy()
            return sanitize_for_gemini(resolved, defs)
        
        new_schema = {}
        
        # Handle anyOf for optionals first
        if "anyOf" in schema:
            types = [sanitize_for_gemini(item, defs) for item in schema["anyOf"]]
            non_nulls = [t for t in types if t.get('type') != 'null']
            if non_nulls:
                new_schema.update(non_nulls[0])
                new_schema["nullable"] = True
                
        # Process the rest of the allowed keys
        for k, v in schema.items():
            if k in ALLOWED_KEYS:
                if k == "properties" and isinstance(v, dict):
                    # v maps property_name -> property_schema
                    new_schema[k] = {
                        prop_name: sanitize_for_gemini(prop_schema, defs)
                        for prop_name, prop_schema in v.items()
                    }
                else:
                    new_schema[k] = sanitize_for_gemini(v, defs)
                
        return new_schema
        
    elif isinstance(schema, list):
        return [sanitize_for_gemini(item, defs) for item in schema]
        
    return schema

def get_gemini_schema() -> dict:
    raw_schema = ArchitectureResponse.model_json_schema()
    defs = raw_schema.get("$defs", {})
    resolved_schema = sanitize_for_gemini(raw_schema, defs)
    
    serialized = json.dumps(resolved_schema)
    assert "$ref" not in serialized, "Found $ref in Gemini schema"
    assert "$defs" not in serialized, "Found $defs in Gemini schema"
    assert "title" not in serialized, "Found title in Gemini schema"
    
    return resolved_schema
