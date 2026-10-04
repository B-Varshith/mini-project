from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .api.predict import router as predict_router

app = FastAPI(
    title="Agentic AI Fraud Detection",
    description="Six-agent claim verification chain with XAI audit trail",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router, prefix="/agentic", tags=["agentic"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "agentic-ai-fraud-detection"}