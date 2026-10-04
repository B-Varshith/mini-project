from app.services.xai_service import log_audit, get_audit_trail
from app.api.predict import predict_fraud
from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.include_router(predict_fraud)

if __name__ == "__main__":
    print("Starting Agentic AI Fraud Detection Service...")
    print("Audit log will be maintained for all agent actions")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=False)