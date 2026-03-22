# swiftdeeds-outreach-pipeline

Internal B2B cold email pipeline automation tool. Acquires targeted leads, cleans and enriches them, then pushes to Instantly.ai for warmup and sending — all from a single web dashboard.

## Pipeline Stages

1. **Sourcing** — Pull targeted contacts via Apollo.io (configurable)
2. **Enrichment** — Verify and enrich contacts via Snov.io (configurable)
3. **Campaign** — Push cleaned contacts to Instantly.ai for warmup and sending (configurable)

Each stage is modular — providers can be swapped via config without touching pipeline logic.

## Stack

- **Backend:** Python + FastAPI
- **Frontend:** React (Vite)
- **Database:** SQLite
- **Local deployment:** Docker Compose

## Getting Started

```bash
cp .env.example .env
# Fill in your API keys

docker compose up
```

Frontend: http://localhost:5173
API: http://localhost:8000

## Environment Variables

See `.env.example` for required API keys (Apollo, Snov, Instantly).
