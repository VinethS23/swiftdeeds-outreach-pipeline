# Swiftdeeds Outreach Pipeline

## What This Is

An internal web dashboard that automates the full B2B cold email workflow for a small team. It sources targeted contacts via Apollo.io, verifies and enriches them through Snov.io, pushes clean leads to Instantly.ai for sending and warmup, and surfaces campaign analytics back into the dashboard.

## Core Value

A campaign runs from target criteria to verified leads in Instantly with zero manual steps — the team sets parameters and the pipeline handles everything.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] User can create a campaign by defining target criteria (industry, job title, location, contact limit)
- [ ] Pipeline automatically sources matching contacts from Apollo.io
- [ ] Pipeline verifies and enriches contacts via Snov.io, dropping invalid emails
- [ ] Pipeline pushes clean contacts to Instantly.ai and triggers campaign sending
- [ ] User can monitor live pipeline progress (sourcing → enriching → sending stages)
- [ ] User can view campaign history with stage outcomes and contact counts
- [ ] User can view campaign analytics (open rates, reply rates from Instantly)
- [ ] User can configure Instantly campaign settings from the dashboard

### Out of Scope

- Multi-tenant / client-facing access — internal team only
- Mobile app — web dashboard only
- Cloud deployment — local Docker Compose for now

## Context

- Replacing a fully manual process — no existing tooling
- Stack already decided: Python + FastAPI backend, React (Vite) frontend, SQLite via SQLModel, Docker Compose
- API integrations: Apollo.io (sourcing), Snov.io (enrichment/verification), Instantly.ai (sending + analytics)
- Free tier constraints during development: Apollo (50 credits/mo), Snov (150 credits/mo)
- Each pipeline stage must be independently swappable via provider config

## Constraints

- **Tech Stack**: Python + FastAPI, React (Vite), SQLite, Docker Compose — already decided, no change
- **APIs**: Apollo.io, Snov.io, Instantly.ai — all three required integrations
- **Deployment**: Local only via Docker Compose — no cloud infrastructure for now
- **Credits**: Apollo 50/mo, Snov 150/mo — keep test runs minimal during development

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| SQLite via SQLModel | Zero-config local setup, no separate DB server needed | — Pending |
| FastAPI background tasks | Simple for current scale, swappable for Celery + Redis later | — Pending |
| Provider abstraction via base classes | Stage providers swappable via env config without code changes | — Pending |

---
*Last updated: 2026-03-22 after initialization*
