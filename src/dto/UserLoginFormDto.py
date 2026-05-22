
from pydantic import BaseModel

class UserLoginFormDto(BaseModel):
    login: str
    password: str