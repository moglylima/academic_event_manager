from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from typing import List
from uuid import UUID, uuid4
from app.schemas.event_schema import EventSchema, EventCreateSchema
from app.services.event_service import (
    write_event,
    read_events,
    update_event_csv,
    delete_event_csv,
    get_csv_hash,
    compress_csv_file,
    count_events
)

router = APIRouter()

@router.get(
    "/events/",
    response_model=dict,
    status_code=200,
    summary="List all events",
    description="Retrieve a list of all events stored in the system. Each event includes details such as title, date, location, capacity, and category."
)
def list_events():
    """
    Retrieve all events stored in the CSV file.
    """
    events = read_events()
    return {
        "status": "success",
        "message": f"{len(events)} event(s) found." if events else "No events found.",
        "data": events
    }


@router.post(
    "/events/",
    response_model=dict,
    status_code=201,
    summary="Create a new event",
    description="Create and register a new event in the system. The event will be assigned a unique ID automatically."
)
def create_event(event: EventCreateSchema):
    """
    Add a new event to the system and store it in the CSV file.
    """
    # Generate a UUID for the new event
    event_to_write = EventSchema(id=uuid4(), **event.dict())
    write_event(event_to_write)
    return {
        "status": "success",
        "message": "Event successfully created.",
        "data": event_to_write
    }


@router.put(
    "/events/{event_id}/",
    response_model=dict,
    status_code=200,
    summary="Update an existing event",
    description="Update the details of an existing event based on its unique ID."
)
def update_event(event_id: UUID, updated_event: EventCreateSchema):
    """
    Update an existing event in the CSV file.
    """
    # Find the existing event
    all_events = read_events()
    existing_event = next((e for e in all_events if e.id == event_id), None)
    if not existing_event:
        raise HTTPException(
            status_code=404,
            detail={"status": "error", "message": "Event not found."}
        )

    # Create an updated event object
    updated_event_with_id = EventSchema(id=event_id, **updated_event.dict())
    update_event_csv(updated_event_with_id)
    return {
        "status": "success",
        "message": "Event successfully updated.",
        "data": updated_event_with_id
    }


@router.delete(
    "/events/{event_id}/",
    response_model=dict,
    status_code=200,
    summary="Delete an event",
    description="Remove an event from the system using its unique ID."
)
def delete_event(event_id: UUID):
    """
    Delete an event from the CSV file.
    """
    try:
        delete_event_csv(event_id)
        return {
            "status": "success",
            "message": "Event successfully deleted."
        }
    except HTTPException:
        raise HTTPException(
            status_code=404,
            detail={"status": "error", "message": "Event not found."}
        )


@router.get(
    "/events/hash/",
    response_model=dict,
    status_code=200,
    summary="Get CSV file hash",
    description="Calculate and return the SHA256 hash of the CSV file containing the events."
)
def get_csv_hash_route():
    """
    Calculate the SHA256 hash of the CSV file.
    """
    hash_value = get_csv_hash()
    return {
        "status": "success",
        "message": "CSV hash calculated successfully.",
        "data": {"sha256": hash_value}
    }


@router.get(
    "/events/compress/",
    status_code=200,
    summary="Download compressed CSV file",
    description="Compress the CSV file containing the events into a ZIP archive and return it as a downloadable file."
)
def compress_csv_route():
    """
    Compress the CSV file and return it as a ZIP file.
    """
    zip_file_path = compress_csv_file()
    return FileResponse(
        zip_file_path,
        media_type="application/zip",
        filename=zip_file_path.split("/")[-1],
        headers={"Content-Disposition": "attachment; filename=event.zip"}
    )


@router.get(
    "/events/count/",
    response_model=dict,
    status_code=200,
    summary="Count all events",
    description="Return the total number of events currently stored in the system."
)
def count_events_route():
    """
    Count the total number of events in the CSV file.
    """
    count = count_events()
    return {
        "status": "success",
        "message": f"{count} event(s) found in the CSV file." if count > 0 else "No events found in the CSV file.",
        "data": {"count": count}
    }
