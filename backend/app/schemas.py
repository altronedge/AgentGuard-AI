from typing import Any, Literal
from pydantic import BaseModel, Field

class ActionRequest(BaseModel):
    agent_id: str = "demo-agent"
    action: str
    parameters: dict[str, Any] = Field(default_factory=dict)
    context: str = ""

class Decision(BaseModel):
    decision: Literal["allow", "log", "approval_required", "block"]
    risk_score: int
    reasons: list[str]
    event_id: str

class ApprovalRequest(BaseModel):
    action: str
    parameters: dict[str, Any]
    approved_by: str = "local-developer"
