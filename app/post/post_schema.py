from pydantic import BaseModel, EmailStr
from datetime import datetime

# - UserCreate → 생성용
# - UserUpdate → 수정용
# - UserResponse → 응답용

class PostCreate(BaseModel):


class PostUpdate(BaseModel):


class PostResponse(BaseModel):