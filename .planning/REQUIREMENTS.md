# Requirements: Swiftdeeds Outreach Pipeline

**Defined:** 2026-03-23
**Core Value:** A campaign runs from target criteria to verified leads in Instantly with zero manual steps.

## v1 Requirements

### Pipeline

- [ ] **PIPE-01**: System sources contacts from Apollo.io based on campaign target criteria (industry, job title, location, contact limit)
- [ ] **PIPE-02**: System verifies and enriches contacts via Snov.io, dropping emails that fail verification
- [ ] **PIPE-03**: System pushes verified contacts to Instantly.ai and triggers campaign sending
- [ ] **PIPE-04**: Pipeline stages run in sequence (sourcing → enriching → sending) as a background task
- [ ] **PIPE-05**: Each pipeline stage is independently swappable via environment variable configuration

### Dashboard

- [ ] **DASH-01**: User can create a campaign by entering target criteria (industry, job title, location, contact limit)
- [ ] **DASH-02**: User can see live pipeline progress while a campaign is running (sourcing → enriching → sending)
- [ ] **DASH-03**: User can view a list of past campaigns with their status and contact counts
- [ ] **DASH-04**: User can view campaign detail showing stage outcomes and contact counts

### Data

- [ ] **DATA-01**: System stores campaign records with criteria, status, and timestamps
- [ ] **DATA-02**: System stores contact records with enrichment data and pipeline stage
- [ ] **DATA-03**: System logs pipeline stage transitions with status and messages per campaign

## v2 Requirements

### Analytics

- **ANLX-01**: User can view open rate and reply rate per campaign (pulled from Instantly API)
- **ANLX-02**: Dashboard shows aggregate outreach performance metrics

### Operations

- **OPER-01**: User can configure Instantly campaign settings from the dashboard
- **OPER-02**: User can re-run a failed pipeline stage without restarting the whole campaign
- **OPER-03**: System maintains a suppression list of previously contacted emails to avoid duplicates
- **OPER-04**: User can export a cleaned contact list as CSV

## Out of Scope

| Feature | Reason |
|---------|--------|
| Multi-tenant / client access | Internal tool only — no auth needed for v1 |
| Cloud deployment | Local Docker Compose only for now |
| Mobile app | Web-first |
| Real-time chat / notifications | Not core to pipeline value |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| PIPE-01 | Phase 1 | Pending |
| PIPE-02 | Phase 1 | Pending |
| PIPE-03 | Phase 1 | Pending |
| PIPE-04 | Phase 1 | Pending |
| PIPE-05 | Phase 1 | Pending |
| DATA-01 | Phase 1 | Pending |
| DATA-02 | Phase 1 | Pending |
| DATA-03 | Phase 1 | Pending |
| DASH-01 | Phase 2 | Pending |
| DASH-02 | Phase 2 | Pending |
| DASH-03 | Phase 2 | Pending |
| DASH-04 | Phase 2 | Pending |

**Coverage:**
- v1 requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0 ✓

---
*Requirements defined: 2026-03-23*
*Last updated: 2026-03-23 after initial definition*
