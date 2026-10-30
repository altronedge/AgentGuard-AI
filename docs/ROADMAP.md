# Roadmap

## Foundation
- [x] FastAPI service and typed request/decision schemas
- [x] Deterministic policy evaluation endpoint
- [x] React dashboard playground
- [x] Docker Compose local environment
- [x] Initial safety unit tests and CI workflow
- [x] Optional OpenAI and Bedrock client factories

## Next increments
1. Persist agents, runs, events, policies, approvals, and audit records in PostgreSQL with migrations.
2. Add authentication, RBAC, and tenant isolation.
3. Build a tool execution gateway with allow-listed tools and strict argument schemas.
4. Bind approvals to exact action hashes and enforce expiry and one-time use.
5. Add richer prompt-injection, PII, and secret detection with configurable policies.
6. Add OpenTelemetry, Prometheus metrics, and Grafana dashboards.
7. Add evaluation datasets, adversarial tests, and model/provider benchmarks.
8. Add signed audit exports and operational deployment hardening.
