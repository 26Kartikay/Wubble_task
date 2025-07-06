from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import run_agent
from dotenv import load_dotenv
load_dotenv
app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask_agent(request: PromptRequest):
    try:
        response = run_agent(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
