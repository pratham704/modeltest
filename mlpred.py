from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins or use "*" for any origin (not recommended for production).
    allow_credentials=True,
    allow_methods=["*"],  # You can specify HTTP methods that are allowed.
    allow_headers=["*"],  # You can specify which HTTP headers are allowed.
)

class ScoringItem(BaseModel):
    Age: int
    Gender: int
    self_employed: int
    family_history: int
    work_interfere: int
    no_employees: int
    remote_work: int
    tech_company: int
    benefits: int
    care_options: int
    wellness_program: int
    seek_help: int
    anonymity: int
    leave: int
    mental_health_consequence: int
    phys_health_consequence: int
    coworkers: int
    supervisor: int
    mental_health_interview: int
    phys_health_interview: int
    mental_vs_physical: int
    obs_consequence: int

@app.post('/')
async def scoring_endpoint(item: ScoringItem):
    with open('main_model_git.pkl', 'rb') as f:
        model = joblib.load(f)

    data = item.dict()
    df = pd.DataFrame([data])
    yhat = model.predict(df)
    return {"prediction": int(yhat)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
