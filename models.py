
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class Action(BaseModel):
    action_type: Literal["view", "redact", "mask", "submit"]
    target_text: Optional[str] = None
    label: Optional[str] = None

class Observation(BaseModel):
    document_chunk: str
    redaction_count: int
    compliance_score: float

class State(BaseModel):
    full_text: str
    ground_truth_pii: List[dict]
    history: List[Action]
