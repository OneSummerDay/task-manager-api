from pydantic import BaseModel

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskDelete(BaseModel):
    id: int


class TaskRead(TaskBase):
    id: int

    class Config:
        orm_mode = True
    
    