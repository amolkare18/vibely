# schemas.py
from pydantic import BaseModel

# Used for incoming request
class User(BaseModel):
    username: str
    fullname:str
    password: str