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

@router.get("/events/", response_model=dict, status_code=200)
def list_events():
    """
    Retorna todos os eventos cadastrados no arquivo CSV.
    """
    events = read_events()
    return {
        "status": "success",
        "message": f"{len(events)} event(s) found." if events else "No events found.",
        "data": events
    }


@router.post("/events/", response_model=dict, status_code=201)
def create_event(event: EventCreateSchema):
    """
    Adiciona um novo evento no arquivo CSV.
    """
    # Gera o UUID para o novo evento
    event_to_write = EventSchema(id=uuid4(), **event.dict())
    write_event(event_to_write)
    return {
        "status": "success",
        "message": "Event successfully created.",
        "data": event_to_write
    }


@router.put("/events/{event_id}/", response_model=dict, status_code=200)
def update_event(event_id: UUID, updated_event: EventCreateSchema):
    """
    Atualiza um evento existente no arquivo CSV.
    """
    # Busca o evento existente
    all_events = read_events()
    existing_event = next((e for e in all_events if e.id == event_id), None)
    if not existing_event:
        raise HTTPException(
            status_code=404,
            detail={"status": "error", "message": "Event not found."}
        )

    # Cria um novo objeto EventSchema com os dados atualizados
    updated_event_with_id = EventSchema(id=event_id, **updated_event.dict())
    update_event_csv(updated_event_with_id)
    return {
        "status": "success",
        "message": "Event successfully updated.",
        "data": updated_event_with_id
    }


@router.delete("/events/{event_id}/", response_model=dict, status_code=200)
def delete_event(event_id: UUID):
    """
    Remove um evento do arquivo CSV.
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


@router.get("/events/hash/", response_model=dict, status_code=200)
def get_csv_hash_route():
    """
    Retorna o hash SHA256 do arquivo CSV.
    """
    hash_value = get_csv_hash()
    return {
        "status": "success",
        "message": "CSV hash calculated successfully.",
        "data": {"sha256": hash_value}
    }


@router.get("/events/compress/", status_code=200)
def compress_csv_route():
    """
    Compacta o arquivo CSV em um arquivo ZIP e retorna o arquivo.
    """
    zip_file_path = compress_csv_file()
    return FileResponse(
        zip_file_path,
        media_type="application/zip",
        filename=zip_file_path.split("/")[-1],
        headers={"Content-Disposition": "attachment; filename=event.zip"}
    )


@router.get("/events/count/", response_model=dict, status_code=200)
def count_events_route():
    """
    Retorna a quantidade de eventos no arquivo CSV.
    """
    count = count_events()
    return {
        "status": "success",
        "message": f"{count} event(s) found in the CSV file." if count > 0 else "No events found in the CSV file.",
        "data": {"count": count}
    }
