from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    
class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = None

class Category(CategoryBase):
    id: int
    
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    stockKeepingUnit: str = Field(..., min_length=3, max_length=50)
    category_id: Optional[int] = None
    image_url: Optional[HttpUrl] = None
    is_active: Optional[bool] = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    stockKeepingUnit: Optional[str] = Field(None, min_length=3, max_length=50)
    category_id: Optional[int] = None
    image_url: Optional[HttpUrl] = None
    is_active: Optional[bool] = None

class ProductInDB(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    category: Optional[Category] = None

    class Config:
        orm_mode = True

class ProductList(BaseModel):
    total: int
    items: List[ProductInDB]

    class Config:
        orm_mode = True