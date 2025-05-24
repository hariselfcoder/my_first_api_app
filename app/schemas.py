from pydantic import BaseModel

# User
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Task
class TaskBase(BaseModel):
    title: str
    description: str = ""

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool
    user_id: int

    model_config = {"from_attributes": True}
