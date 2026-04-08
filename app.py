from fastapi import FastAPI
from models import Action, Observation

app = FastAPI()

# IMPORTANT: Must be @app.post, not @app.get
@app.post("/reset")
def reset():
    # Your reset logic here
    return {"document_chunk": "Initial text", "redaction_count": 0, "compliance_score": 0.0}

@app.post("/step")
def step(action: Action):
    # Your step logic here
    return {
        "observation": {"document_chunk": "Updated text", "redaction_count": 1, "compliance_score": 0.5},
        "reward": 0.5,
        "done": False
    }
