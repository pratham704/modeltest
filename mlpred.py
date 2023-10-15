from fastapi import FastAPI, Query, HTTPException
import pandas as pd
import joblib

app = FastAPI()

with open('main_model_git.pkl', 'rb') as f:
    model = joblib.load(f) 
 


@app.get("/")
async def root():
    return {"message": "Hey, I'm here!"}



@app.get("/bro")
async def root():
    return {"message": "wassup"}







