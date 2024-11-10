from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    
    products = relationship("Product", back_populates="category")
    
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True , index = True)
    name = Column(String , index=True, nullable=True)
    description= Column(Text)
    price = Column(Float , nullable=False)
    stock = Column(Integer, default=0)
    stockKeepingUnit = Column(String, unique=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    image_url = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    category = relationship("Category", back_populates="products")
    
    def __repr__(self):
        return f"<Product {self.name}"