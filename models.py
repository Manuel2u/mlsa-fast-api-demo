from pydantic import BaseModel
from typing import Optional

class Books(BaseModel):
    id : Optional[int]
    title : str
    author: str
    pages : int