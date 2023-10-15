from fastapi import FastAPI, Query, HTTPException
import pandas as pd
import joblib

app = FastAPI()




class ScoringItem(BaseModel):
    Age: int                        
    Gender: int                      
    self_employed: int               
    family_history: int                                
    work_interfere : int             
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


@app.post('/pred')
async def scorinng_endpoints(item:ScoringItem):
      
    with open('main_model_git.pkl','rb') as f:
       model=joblib.load(f)

    df=pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat=model.predict(df)
    return {"prediction": int(yhat)}





@app.get("/")
async def root():
    return {"message": "Hey, I'm here!"}



@app.get("/bro")
async def root():
    return {"message": "wassup"}







