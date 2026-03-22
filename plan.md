# Swiftdeeds Outreach Pipeline

## Overview
An internal web dashboard that automates the full B2B cold email pipeline — from lead acquisition to sending. Built for a small marketing team to run campaigns without any manual steps.

## Problem
Running a B2B cold email campaign requires manually sourcing leads, cleaning and enriching them, warming up email accounts, and sending — a process that is slow, inconsistent, and doesn't scale. Every campaign requires someone to coordinate multiple tools by hand, which introduces errors and limits throughput.

## Tech Stack
- **Frontend:** React (Vite) — lightweight, fast dev experience, sufficient for a dashboard UI
- **Backend:** Python + FastAPI — best ecosystem for API orchestration and data processing; async-native
- **Database:** SQLite (via SQLModel) — zero-config local setup, no separate DB server needed
- **Task execution:** FastAPI background tasks — simple enough for current scale, swappable for Celery + Redis if volume grows
- **Local deployment:** Docker Compose — one command to start everything, works for any team member
- **External APIs:** Apollo.io (sourcing), Snov.io (enrichment), Instantly.ai (warmup + sending)

## Architecture
The pipeline runs as a series of async stages triggered from the dashboard. When a user creates a campaign (defining target audience criteria), the backend calls Apollo.io to fetch matching contacts, passes them to Snov.io for verification and enrichment, then pushes the cleaned list to Instantly.ai which handles warmup and sending. Each stage updates a status record in SQLite so the dashboard shows live progress. Each pipeline stage sits behind an abstract base class — swapping providers (e.g. Apollo → Hunter.io, Snov → ZeroBounce, Instantly → another sender) requires only a new implementation with no changes to orchestration logic. The active provider per stage is set via environment config.

## Features

### Must-Have
- **Campaign creation:** User defines target criteria (industry, job title, location, contact limit) and submits a campaign from the dashboard.
- **Apollo.io sourcing:** Backend calls Apollo API with campaign criteria and returns matching contacts. Respects credit limits.
- **Snov.io enrichment:** Passes sourced contacts to Snov for email verification and basic enrichment (name, title, company). Drops invalid emails.
- **Instantly.ai campaign push:** Creates a campaign in Instantly, uploads verified contacts, and triggers sending. Instantly handles warmup automatically.
- **Pipeline status dashboard:** Shows each campaign's live progress through sourcing → enrichment → campaign stages, with contact counts at each step.
- **Campaign history:** List of past campaigns with stage outcomes and contact counts.

### Nice-to-Have
- **Per-campaign analytics:** Pull open rate and reply rate from Instantly API and display on campaign detail view.
- **Re-run failed stages:** Retry a specific failed stage without restarting the whole pipeline.
- **Suppression list:** Track previously contacted emails to avoid duplicate outreach across campaigns.
- **CSV export:** Download the cleaned, enriched contact list from any campaign.

## Data Model
- **Campaign:** id, name, target_criteria (JSON), status (pending/sourcing/enriching/pushing/complete/failed), created_at
- **Contact:** id, campaign_id, email, first_name, last_name, title, company, linkedin_url, verified (bool), stage (sourced/enriched/pushed), created_at
- **PipelineLog:** id, campaign_id, stage, status, message, timestamp

## API / Integration Contracts
- **Apollo.io** — POST `/v1/mixed_people/search` with criteria filters; returns contact list
- **Snov.io** — OAuth2 token exchange, then POST `/v1/get-emails-verification-status`; returns validation status per email
- **Instantly.ai** — POST `/api/v1/campaign/create`, POST `/api/v1/lead/add`, POST `/api/v1/campaign/launch`

## Auth
No auth required — local deployment, trusted internal team only.

## Deployment
Local only via Docker Compose. Run `docker compose up` to start backend (port 8000) and frontend (port 5173). API keys configured in `.env`.

## Constraints
- Must operate within free tier limits: Apollo (50 credits/mo), Snov (150 credits/mo) during testing phase
- Local deployment only — no cloud infrastructure for now

## Development Phases

### Phase 1 — Foundation & Pipeline Core
- [ ] Set up SQLite database schema with SQLModel (`Campaign`, `Contact`, `PipelineLog` models)
- [ ] `GET /campaigns` — list all campaigns with status
- [ ] `POST /campaigns` — create a new campaign with target criteria
- [ ] `GET /campaigns/{id}` — get campaign detail with contacts and logs
- [ ] Implement `SourcingProvider` base class and `ApolloSourcingProvider` — calls Apollo search API, maps response to `Contact` schema
- [ ] Implement `EnrichmentProvider` base class and `SnovEnrichmentProvider` — Snov OAuth token fetch, verify contacts, drop invalids
- [ ] Implement `CampaignProvider` base class and `InstantlyCampaignProvider` — create Instantly campaign, upload leads, launch
- [ ] Pipeline orchestrator: `run_pipeline(campaign_id)` — chains sourcing → enrichment → campaign, updates `Campaign.status` and writes `PipelineLog` entries at each stage
- [ ] Wire pipeline orchestrator as a FastAPI background task triggered on campaign creation
- [ ] Provider config: load active provider per stage from environment variables

### Phase 2 — Dashboard UI
- [ ] Campaign list view: table of campaigns with name, status, contact counts, created date
- [ ] Campaign creation form: fields for industry, job title, location, contact limit
- [ ] Campaign detail view: stage-by-stage progress breakdown with contact count at each step and log entries
- [ ] Live status polling: dashboard refreshes campaign status every 10 seconds while a pipeline is running
- [ ] Basic error display: show failed stage and error message on campaign detail

### Phase 3 — Analytics & Quality of Life
- [ ] Pull open rate and reply rate from Instantly API and display on campaign detail
- [ ] Re-run failed stage button on campaign detail
- [ ] Suppression list: store contacted emails in DB, skip duplicates in future campaigns
- [ ] CSV export endpoint and download button for cleaned contact list

## Open Questions
- Does Instantly.ai's API support programmatic campaign creation and lead upload? Verify endpoint availability and rate limits before Phase 1 implementation.
- Snov.io per-contact verification may be slow at scale — investigate batch verification endpoint to speed up enrichment stage.
