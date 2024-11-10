from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from ..db.database import get_db
from ..models.user import User
from ..schemas.user import UserCreate, UserResponse, Token
from ..utils.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_active_user
)
from ..config.settings import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db:Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
        
    if db.query(User).filter(User.username == user_in.username).first():
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    user = User(
        email= user_in.email,
        username= user_in.username,
        hashed_password= get_password_hash(user_in.password)
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@router.post("/login", response_model=Token)
async def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.__dict__['hashed_password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate":"Bearer"}
        )
    
    access_token_expires = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub":user.email},
        expires_delta= access_token_expires
    )
    
    return {"access_token": access_token, "token_type":"bearer"}

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

