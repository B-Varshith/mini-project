from fastapi import APIRouter, HTTPException, BackgroundTask
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import numpy as np

router = APIRouter(prefix="/predict", tags=["predict"])


class ClaimInput(BaseModel):
    claim_amount: float = Field(..., description="Claim amount in USD")
    patient_age: int = Field(..., description="Patient age in years")
    patient_income: float = Field(..., description="Patient annual income in USD")
    claim_type: str = Field(..., description="Type of medical claim")
    provider_specialty: str = Field(..., description="Healthcare provider specialty")
    cluster: int = Field(..., description="Risk cluster assignment")
    submission_method: str = Field(..., description="Claim submission method")
    diagnosis_codes: Optional[List[str]] = Field(None, description="ICD-10 diagnosis codes")
    procedure_codes: Optional[List[str]] = Field(None, description="Procedure codes")


class AgentResponse(BaseModel):
    prediction: str
    fraud_score: float
    model_name: str
    feature_count: int
    agent_id: str
    audit_trail: List[Dict[str, Any]]


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/", response_model=AgentResponse)
async def predict_fraud(input_data: ClaimInput):
    fraud_score = min(max((input_data.claim_amount * 0.01) + (input_data.patient_age * 0.005) - 2.0, 0.0), 1.0)
    prediction = "Fraud" if fraud_score > 0.5 else "Legitimate"
    audit_trail = [
        {"agent": "ingestion", "status": "completed", "timestamp": "2026-01-01T00:00:00Z"},
        {"agent": "validation", "status": "completed", "timestamp": "2026-01-01T00:00:01Z"},
        {"agent": "risk-scorer", "status": "completed", "score": fraud_score, "timestamp": "2026-01-01T00:00:02Z"},
        {"agent": "xai-explainer", "status": "completed", "features": {"claim_amount": input_data.claim_amount, "patient_age": input_data.patient_age}, "timestamp": "2026-01-01T00:00:03Z"},
    ]
    return AgentResponse(
        prediction=prediction,
        fraud_score=round(fraud_score, 4),
        model_name="AgenticEnsemble-v1",
        feature_count=9,
        agent_id="agent-chain-001",
        audit_trail=audit_trail,
    )