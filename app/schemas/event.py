from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    id: Optional[int] = Field(default=None, alias='_id')
    title: str
    date: datetime
    location: str
    capacity: int
