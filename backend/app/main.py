from fastapi import FastAPI
from app.routers import resume
app=FastAPI()

app.include_router(
    resume.router,
    prefix="/resume",
    tags=["resume"]
)

@app.get("/") #decorator,A function that modifies another function's behavior without changing the function itself.
def home():
    return{
        "message":"Api Running"
    }