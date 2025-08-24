from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app import models, crud

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo List API")

@app.get("/")
def read_root():
    return {"message": "Hello, Thiago! Python is working!"}

@app.get("/tasks/")
def list_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/")
def create_task(title: str, description: str = None, db: Session = Depends(get_db)):
    return crud.create_task(db, title=title, description=description)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str = None, description: str = None, completed: bool = None, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id=task_id, title=title, description=description, completed=completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}