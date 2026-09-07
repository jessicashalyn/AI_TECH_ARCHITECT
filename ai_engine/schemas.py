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
