from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

# Essas classes definem como os usuários
# enviam dados para a API
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)

# Essas classes definem a forma com que a
# API retorna dados para os usuários.
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    class Config:
        orm_mode = True

class PostWithVotes(BaseModel):
    Post: PostResponse
    votes: int
    class Config:
        orm_mode = True