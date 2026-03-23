# Roadmap: Swiftdeeds Outreach Pipeline

## Overview

Three phases deliver the full pipeline: first, a working project scaffold with data models and provider abstraction; second, the three API integrations running as a background pipeline from Apollo sourcing through Snov enrichment to Instantly sending; third, a React dashboard that lets the team create campaigns, watch live progress, and review history. By the end of Phase 3, a campaign runs from target criteria to verified leads in Instantly with zero manual steps.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Foundation** - Project scaffold, data models, Docker Compose, and provider abstraction layer
- [ ] **Phase 2: Pipeline Engine** - Apollo sourcing, Snov enrichment, and Instantly sending running as a sequenced background task
- [ ] **Phase 3: Dashboard** - React frontend for campaign creation, live progress monitoring, history, and detail views

## Phase Details

### Phase 1: Foundation
**Goal**: The project runs locally in Docker Compose with all data models in place and provider interfaces defined so the pipeline has a stable base to build on
**Depends on**: Nothing (first phase)
**Requirements**: PIPE-05, DATA-01, DATA-02, DATA-03
**Success Criteria** (what must be TRUE):
  1. `docker compose up` starts the FastAPI backend and React frontend with no errors
  2. The database schema exists with tables for campaigns, contacts, and stage logs
  3. A campaign record can be created, read, and updated via the API with criteria, status, and timestamps
  4. Contact records store enrichment data and current pipeline stage
  5. Stage transition logs are written with status and message per campaign
**Plans**: TBD

### Phase 2: Pipeline Engine
**Goal**: A campaign trigger causes the system to source contacts from Apollo, verify and enrich them via Snov, push clean contacts to Instantly, and trigger sending — all as a single background task with no manual steps
**Depends on**: Phase 1
**Requirements**: PIPE-01, PIPE-02, PIPE-03, PIPE-04
**Success Criteria** (what must be TRUE):
  1. Calling the campaign trigger API causes contacts to be sourced from Apollo matching the target criteria
  2. Each sourced contact passes through Snov verification — invalid emails are dropped and not forwarded
  3. Verified contacts are pushed to Instantly and campaign sending is triggered
  4. Stages run in sequence (sourcing → enriching → sending) without manual intervention between them
  5. Swapping a provider via environment variable config changes which integration handles that stage without code changes
**Plans**: TBD

### Phase 3: Dashboard
**Goal**: Team members can use the web dashboard to create campaigns, watch the pipeline run in real time, and review the history and outcomes of past campaigns
**Depends on**: Phase 2
**Requirements**: DASH-01, DASH-02, DASH-03, DASH-04
**Success Criteria** (what must be TRUE):
  1. User can fill out a form with industry, job title, location, and contact limit and submit it to create and start a campaign
  2. While a campaign is running, the dashboard shows the current pipeline stage (sourcing / enriching / sending) updating live
  3. User can open a list of all past campaigns and see the status and contact counts for each
  4. User can click into a campaign to see per-stage outcomes and contact counts
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 0/TBD | Not started | - |
| 2. Pipeline Engine | 0/TBD | Not started | - |
| 3. Dashboard | 0/TBD | Not started | - |
