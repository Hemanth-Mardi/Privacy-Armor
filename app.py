
from fastapi import FastAPI
from models import Action
from server.privacy_environment import PrivacyEnvironment
from server.ui import get_ui

app = FastAPI()
env = PrivacyEnvironment()

@app.get("/")
def home():
    return get_ui()

@app.api_route("/reset", methods=["GET", "POST"])
@app.api_route("/reset/", methods=["GET", "POST"])
def reset(difficulty: str = "easy"):
    return env.reset(difficulty)

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}