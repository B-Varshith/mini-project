from typing import Dict, Any, List
import json
import time
import hashlib


class XAIExplainer:
    def explain_prediction(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        features = {}
        for key, value in input_data.items():
            features[key] = {"value": value, "impact": self._calculate_impact(key, value)}
        return {"feature_importances": features, "method": "shap-approximation"}

    def _calculate_impact(self, feature: str, value: Any) -> float:
        base_impacts = {
            "claim_amount": 0.3,
            "patient_age": 0.15,
            "patient_income": 0.1,
            "cluster": 0.25,
        }
        return base_impacts.get(feature, 0.05)


audit_log: List[Dict[str, Any]] = []
explainer = XAIExplainer()


def log_audit(agent: str, status: str, details: Dict[str, Any] = None) -> str:
    entry = {
        "agent": agent,
        "status": status,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "details": details or {},
    }
    entry["id"] = hashlib.sha256(
        f"{agent}{time.time()}{details}".encode()
    ).hexdigest()[:12]
    audit_log.append(entry)
    return entry["id"]


def get_audit_trail() -> List[Dict[str, Any]]:
    return audit_log