from pydantic import BaseModel, Field
from uuid import UUID

class EventCreateSchema(BaseModel):
    title: str = Field(..., max_length=100)
    date: str  # DD-MM-YYYY
    location: str = Field(..., max_length=150)
    capacity: int
    category: str

class EventSchema(EventCreateSchema):
    id: UUID
