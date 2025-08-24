from app.database import SessionLocal, Base, engine
from app import models, crud

#guarantee the database tables are created
Base.metadata.create_all(bind=engine)

#create a new database session for testing
db = SessionLocal()

#create a new task
new_task = crud.create_task(db, title="Test Task", description="This is a test task.")
print(f"Created Task: {new_task.id}, {new_task.title}, {new_task.description}, {new_task.completed}")

tasks = crud.get_tasks(db)
print("All Tasks:")
for t in tasks:
    print(t.id, t.title, t.description, t.completed)

#update the task
updated_task = crud.update_task(db, task_id=new_task.id, completed=True)
print(f"Updated Task: {updated_task.id}, {updated_task.title}, {updated_task.description}, {updated_task.completed}")

#delete the task
deleted_task = crud.delete_task(db, task_id=new_task.id)
print(f"Deleted Task: {deleted_task.id}, {deleted_task.title}, {deleted_task.description}, {deleted_task.completed}")

db.close()
