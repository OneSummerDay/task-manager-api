from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    is_done: bool = False
    
class TaskCreate(TaskBase):
    pass 

class TaskDelete(BaseModel):
    id: int
    
    class Config:
        orm_mode = True
    
    