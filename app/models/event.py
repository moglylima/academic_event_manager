from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class event(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    data: datetime
    location: str
    max_capacity: int