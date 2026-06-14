from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateSchema(BaseModel):
    fullname: str
    email: EmailStr


class UserUpdateSchema(BaseModel):
    fullname: Optional[str] = None
    email:Optional[EmailStr] = None

    model_config = {
        "extra": "forbid" # no permite campos basura
    }

class UserResponseSchema(BaseModel):
    id: int
    fullname: str
    email: EmailStr

    class Config:
        from_attributes = True