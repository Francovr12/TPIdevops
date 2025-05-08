from fastapi import APIRouter, HTTPException
from app.models.task import Task

router = APIRouter()

# Base de datos simulada
tasks_db = []

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks_db

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
