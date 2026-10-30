import re
from uuid import uuid4
from .schemas import ActionRequest, Decision

SECRET_PATTERNS = [re.compile(r"(?i)(api[_-]?key|secret|password|token)\\s*[:=]\\s*['\\\"]?([A-Za-z0-9_\\-]{12,})")]
PII_EMAIL = re.compile(r"\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}\\b", re.I)
INJECTION_TERMS = ("ignore previous instructions", "reveal system prompt", "developer message", "bypass safety")
DESTRUCTIVE = {"delete_database", "drop_table", "delete_all_files", "disable_security"}


def evaluate(req: ActionRequest) -> Decision:
    reasons: list[str] = []
    text = f"{req.action} {req.context} {req.parameters}".lower()
    score = 0
    if any(term in text for term in INJECTION_TERMS):
        score += 35; reasons.append("Prompt-injection indicator detected")
    if any(p.search(text) for p in SECRET_PATTERNS):
        score += 35; reasons.append("Possible secret in action payload")
    if PII_EMAIL.search(text):
        score += 15; reasons.append("Email address detected in payload")
    if req.action in DESTRUCTIVE:
        score += 60; reasons.append("Destructive action requires approval")
    if req.action.startswith("admin_"):
        score += 50; reasons.append("Privileged action")
    score = min(score, 100)
    if req.action in {"execute_shell", "run_sql", "admin_root"}:
        decision = "block"; reasons.append("This starter does not permit arbitrary shell, SQL, or root actions")
    elif score >= 70:
        decision = "block"
    elif score >= 40:
        decision = "approval_required"
    elif score >= 20:
        decision = "log"
    else:
        decision = "allow"
    return Decision(decision=decision, risk_score=score, reasons=reasons or ["No configured risk indicators"], event_id=str(uuid4()))
