# Security model and current limitations

## Enforcement boundary

The safety API evaluates proposed actions. It is not yet a tool-execution proxy. Do not connect agents to real tools until every tool call is routed through an enforcement gateway that checks policy immediately before execution.

## Current checks

- Simple prompt-injection phrase indicators
- Basic email and credential-pattern detection
- Explicit deny-list for shell, SQL, and root execution
- Risk scoring and approval-required decisions for destructive and privileged actions

These checks are heuristic and can produce false positives and false negatives. They are not a substitute for a dedicated DLP system, sandboxing, identity, or least-privilege controls.

## Production requirements

- Authenticate users and agents; authorise every API request.
- Store approvals bound to an immutable action hash, parameters, actor, expiry, and one-time nonce.
- Fail closed when policy or approval services are unavailable.
- Enforce tool allow-lists and per-agent scopes at the execution boundary.
- Add durable audit storage, tamper-evident logs, rate limits, secret vault integration, and monitoring.
- Never treat model output as trusted policy or permission.
- Do not expose the demo approval endpoint publicly.
