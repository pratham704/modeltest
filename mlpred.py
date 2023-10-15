from fastapi import FastAPI, Query, HTTPException
import pandas as pd
import joblib

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hey, I'm here!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
