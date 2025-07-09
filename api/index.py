from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Vercel! If you see this, your FastAPI serverless function works."}

handler = Mangum(app) 