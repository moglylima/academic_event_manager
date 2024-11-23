from fastapi import APIRouter, HTTPException, status
from app.schemas.event import Event

router = APIRouter()

# Lista em memória para armazenar eventos
events = []


# Create event
@router.post("/", response_model=Event,  status_code=status.HTTP_201_CREATED)
def create_event(event: Event):
    event.id = len(events) + 1
    events.append(event)
    return event

# Get all events
@router.get("/", response_model=list[Event])
def get_events():
    return events

# Get event by id
@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int):
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

# Update event
@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, updated_event: Event):
    for index, event in enumerate(events):
        if event.id == event_id:
            updated_event.id = event.id
            events[index] = updated_event
            return updated_event
    raise HTTPException(status_code=404, detail="Event not found")

# Delete event
@router.delete("/{event_id}", response_model=dict)
def delete_event(event_id: int):
    for index, event in enumerate(events):
        if event.id == event_id:
            events.pop(index)
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Event not found")


# GET /api/events/
