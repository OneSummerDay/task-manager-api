from fastapi import APIRouter, HTTPException
from app.models.task import Task

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello from router!"}

tasks:list[Task] = []

@router.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {'message': 'Task created successfully', 'task': task}


@router.get("/tasks")
def get_all_tasks():
    return tasks


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/task/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return {"message": "Task updated", "task": updated_task}
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/task/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
    raise HTTPException(status_code=404, detail="Task not found")
