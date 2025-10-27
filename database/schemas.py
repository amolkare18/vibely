# schemas.py
from pydantic import BaseModel,Field
from datetime import datetime
from typing import List

# Used for incoming request
class User(BaseModel):
    username: str
    fullname:str
    password: str




class Res(BaseModel):
    user_id:str
    prompt: str                      # e.g. "music", "ebook", "article"
    api_list: List[str]                # list of API URLs or endpoints
    created_at: datetime = Field(default_factory=datetime.utcnow)
  