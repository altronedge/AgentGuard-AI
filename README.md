# AgentGuard AI

An AI agent safety and governance platform for local development. AgentGuard provides a FastAPI policy gateway, risk assessment, prompt-injection and sensitive-data checks, approval gates, audit events, and a React dashboard.

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

- API: http://localhost:8000
- API docs: http://localhost:8000/docs
- Dashboard: http://localhost:5173

The initial release runs safely in demo mode. Model provider credentials are optional and are not required for the safety API or dashboard.

## Safety design

All proposed tool actions are evaluated by the policy engine before execution. This starter release deliberately does not execute arbitrary shell commands, SQL, or external tools. High-risk actions require explicit approval; critical permission violations are blocked. The demo approval endpoint is intended for local development only and must be replaced with authenticated, identity-bound approvals before production use.

## Configuration

See `.env.example`. OpenAI and AWS Bedrock are configured as optional model providers for subsequent agent-runtime integration.

## Tests

```bash
cd backend
python -m pytest
```

## License

MIT
