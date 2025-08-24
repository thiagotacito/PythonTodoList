from fastapi import FastAPI
from app.database import engine, Base
from app import models

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo List API")

@app.get("/")
def read_root():
    return {"message": "Hello, Thiago! Python is working!"}