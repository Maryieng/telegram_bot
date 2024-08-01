from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    text: str
    author: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
