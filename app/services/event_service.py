import csv
import os
from uuid import UUID
from typing import List
from fastapi import HTTPException
from app.schemas.event_schema import EventSchema
from app.utils.file_utils import generate_csv_hash, zip_csv_file
from app.config import CSV_FILE_PATH

# Caminho do arquivo CSV
CSV_FILE = CSV_FILE_PATH


def ensure_csv():
    """
    Garante que o arquivo CSV tenha o cabeçalho correto.
    Reescreve o cabeçalho se o arquivo estiver ausente, vazio ou com cabeçalho incorreto.
    """
    expected_headers = ["id", "title", "date", "location", "capacity", "category"]

    # Caso o arquivo não exista, cria com o cabeçalho correto
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(expected_headers)
        return

    # Caso o arquivo exista, verifica se o cabeçalho está correto
    with open(CSV_FILE, mode="r+", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        first_row = next(reader, None)  # Lê a primeira linha (cabeçalho ou vazio)

        # Se o cabeçalho está ausente ou mal formatado, reescreve
        if not first_row or first_row != expected_headers:
            file.seek(0)
            writer = csv.writer(file)
            writer.writerow(expected_headers)
            remaining_rows = list(reader)  # Salva as linhas restantes (se houver)
            for row in remaining_rows:
                writer.writerow(row)
            file.truncate()  # Remove qualquer dado remanescente após reescrever


def read_events() -> List[EventSchema]:
    """
    Lê todos os eventos do arquivo CSV.
    Garante que o cabeçalho esteja presente antes de tentar ler os registros.
    """
    ensure_csv()  # Garante que o arquivo e o cabeçalho estejam prontos
    events = []
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                event = EventSchema(
                    id=UUID(row["id"]),
                    title=row["title"],
                    date=row["date"],
                    location=row["location"],
                    capacity=int(row["capacity"]),
                    category=row["category"]
                )
                events.append(event)
            except (KeyError, ValueError, Exception) as e:
                print(f"Skipping invalid row: {row}. Error: {e}")
    return events


def write_event(event: EventSchema):
    """
    Adiciona um evento ao arquivo CSV.
    Garante que o cabeçalho esteja presente antes de adicionar o registro.
    """
    ensure_csv()  # Garante que o cabeçalho esteja presente
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([event.id, event.title, event.date, event.location, event.capacity, event.category])


def update_event_csv(updated_event: EventSchema):
    """
    Atualiza um evento no arquivo CSV.
    Garante que o cabeçalho esteja presente antes de reescrever o arquivo.
    """
    events = read_events()
    ensure_csv()  # Garante que o cabeçalho esteja presente
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title", "date", "location", "capacity", "category"])  # Cabeçalho
        for event in events:
            if event.id == updated_event.id:
                writer.writerow([updated_event.id, updated_event.title, updated_event.date,
                                 updated_event.location, updated_event.capacity, updated_event.category])
            else:
                writer.writerow([event.id, event.title, event.date, event.location,
                                 event.capacity, event.category])


def delete_event_csv(event_id: UUID):
    """
    Remove um evento do arquivo CSV.
    Garante que o cabeçalho esteja presente antes de reescrever o arquivo.
    """
    events = read_events()
    event_found = False
    ensure_csv()  # Garante que o cabeçalho esteja presente

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title", "date", "location", "capacity", "category"])  # Cabeçalho

        for event in events:
            if event.id == event_id:
                event_found = True
                continue  # Ignora o evento a ser excluído
            writer.writerow([event.id, event.title, event.date, event.location, event.capacity, event.category])

    if not event_found:
        raise HTTPException(status_code=404, detail="Event not found.")


def get_csv_hash() -> str:
    """
    Retorna o hash SHA256 do arquivo CSV.
    """
    return generate_csv_hash(CSV_FILE)


def compress_csv_file() -> str:
    """
    Compacta o arquivo CSV em um arquivo ZIP.
    """
    return zip_csv_file(CSV_FILE)

def count_events() -> int:
    """
    Conta o número de eventos no arquivo CSV.
    Garante que o cabeçalho esteja presente antes de realizar a contagem.
    """
    ensure_csv()  # Garante que o arquivo e o cabeçalho estão corretos
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return sum(1 for _ in reader)  # Conta o número de linhas no arquivo CSV
