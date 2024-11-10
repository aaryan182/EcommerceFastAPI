from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime
from typing_extensions import Annotated

Username = Annotated[str, constr(min_length=3, max_length=50)]

class UserBase(BaseModel):
    email: EmailStr
    username: Username

class UserCreate(UserBase):
    password: Annotated[str, constr(min_length=8)]
    
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[Username] = None  
    password: Optional[Annotated[str, constr(min_length=8)]] = None
    is_active: Optional[bool] = None
    
class UserInDB(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config: 
        orm_mode = True
    
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config: 
        orm_mode = True
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None