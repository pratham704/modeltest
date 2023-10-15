from fastapi import FastAPI, Query, HTTPException
import pandas as pd
import joblib

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hey, I'm here!"}



@app.get("/bro")
async def root():
    return {"message": "wassup"}







