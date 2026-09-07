from pydantic import BaseModel, Field
from typing import List, Optional

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

def _inline_refs(schema, defs):
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_path = schema["$ref"]
            def_name = ref_path.split("/")[-1]
            resolved = defs.get(def_name, {}).copy()
            return _inline_refs(resolved, defs)
        
        new_schema = {}
        for k, v in schema.items():
            if k == "$defs":
                continue
            if k == "anyOf":
                types = [_inline_refs(item, defs) for item in v]
                non_nulls = [t for t in types if t.get('type') != 'null']
                if non_nulls:
                    new_schema.update(non_nulls[0])
                    new_schema["nullable"] = True
                continue
            new_schema[k] = _inline_refs(v, defs)
        return new_schema
    elif isinstance(schema, list):
        return [_inline_refs(item, defs) for item in schema]
    return schema

def get_gemini_schema() -> dict:
    raw_schema = ArchitectureResponse.model_json_schema()
    defs = raw_schema.get("$defs", {})
    resolved_schema = _inline_refs(raw_schema, defs)
    if "$defs" in resolved_schema:
        del resolved_schema["$defs"]
    return resolved_schema
