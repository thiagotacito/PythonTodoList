from sqlalchemy.orm import Session
from app import models

#list all tasks
def get_tasks(db: Session):
    return db.query(models.Task).all()

# get a specific task by id
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# create a new task
def create_task(db: Session, title: str, description: str = None):
    db_task = models.Task(title=title, description=description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#update an existing task
def update_task(db: Session, task_id: int, title: str = None, description: str = None, completed: bool = None):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed
    db.commit()
    db.refresh(task)

    return task

# delete a task
def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if not task:
        return None 
    db.delete(task)
    db.commit()
    return task