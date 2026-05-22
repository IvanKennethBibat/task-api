from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas


router = APIRouter()

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.title is not None:
        updated_task.title = task.title
    if task.completed is not None:
        updated_task.completed = task.completed

    db.commit()
    db.refresh(updated_task)
    return updated_task

@router.delete("/tasks/{task_id}", response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(deleted_task)
    db.commit()
    return deleted_task

