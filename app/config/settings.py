from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseModel):
    #Database_url
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/ecomm"
    
    #JWT settings
    SECRET_KEY: str = "aaryan"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    #API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "E-commerce API"
    
    class Config: 
        case_sensitive = True
        env_file = ".env"
    
@lru_cache()
def get_settings():
    # using lru_cache to prevent multiple reads of .env file
    return Settings()

settings = get_settings()