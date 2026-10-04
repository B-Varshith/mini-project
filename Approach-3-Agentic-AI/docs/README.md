# Approach 3: Agentic AI Fraud Detection

## Overview
Six-agent claim verification chain with XAI (eXplainable AI) audit trail.

## Agents
1. **Ingestion Agent** - Validates and normalizes input claims
2. **Validation Agent** - Checks for data quality and completeness
3. **Risk Scorer Agent** - Computes fraud probability using ensemble model
4. **XAI Explainer Agent** - Generates explainable insights for each prediction
5. **Decision Agent** - Makes final fraud/legitimate determination
6. **Audit Agent** - Maintains immutable audit trail of all actions

## API Endpoints
- `GET /agentic/health` - Service health check
- `POST /agentic/predict` - Predict fraud likelihood with full audit trail

## Configuration
- Service runs on port 8020
- 29-feature contract frozen from Approach 1
- Class weighting for 6% fraud rate

## Development
- See `PROJECT_PROGRESS.md` for status
- Owned by Varshith (Agentic AI team)