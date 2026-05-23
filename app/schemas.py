from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

class TaskCreate(BaseModel):
    title: str

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    completed: bool

class TaskUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: Optional[str] = None
    completed: Optional[bool] = None

class UserCreate(BaseModel):
    username: str 
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def password_must_contain_special(cls, v):
        special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(char in special_characters for char in v):
            raise ValueError("Password needs at least one special character.")
        
        return v

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str