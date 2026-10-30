from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .schemas import ActionRequest, ApprovalRequest
from .safety import evaluate

app = FastAPI(title="AgentGuard AI", version="0.1.0", description="Local AI agent safety and governance API")
app.add_middleware(CORSMiddleware, allow_origins=[x.strip() for x in settings.cors_origins.split(",")], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok", "service": "agentguard-api", "version": "0.1.0"}

@app.post("/api/v1/safety/evaluate")
def evaluate_action(request: ActionRequest):
    return evaluate(request).model_dump()

@app.post("/api/v1/approvals/demo")
def demo_approval(request: ApprovalRequest):
    # Demo only: never use this unauthenticated endpoint for production authorisation.
    return {"status": "recorded_demo_only", "approved_by": request.approved_by, "action": request.action, "notice": "Not a production identity-bound approval."}
