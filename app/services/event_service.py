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

# Definimos o cabeçalho padrão para o arquivo CSV
HEADERS = ["id", "title", "date", "location", "capacity", "category"]


def ensure_csv():
    """
    Garante que o arquivo CSV tenha o cabeçalho correto.
    Se o arquivo não existir ou estiver vazio, cria um novo com o cabeçalho padrão.
    """
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        # Abre o arquivo em modo escrita ('w') e insere o cabeçalho
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)  # Escreve o cabeçalho


def read_events() -> List[EventSchema]:
    """
    Lê todos os eventos do arquivo CSV e retorna uma lista de objetos EventSchema.
    """
    ensure_csv()  # Garante que o arquivo CSV está configurado corretamente
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Lê o arquivo como dicionários baseados no cabeçalho
        # Converte cada linha em um objeto EventSchema
        return [
            EventSchema(
                id=UUID(row["id"]),
                title=row["title"],
                date=row["date"],
                location=row["location"],
                capacity=int(row["capacity"]),
                category=row["category"]
            )
            for row in reader  # Itera sobre as linhas
        ]


def write_event(event: EventSchema):
    """
    Adiciona um novo evento ao arquivo CSV.
    """
    ensure_csv()  # Garante que o arquivo CSV está configurado corretamente
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)  # Abre o arquivo no modo de adição ('a')
        # Escreve os dados do evento
        writer.writerow([event.id, event.title, event.date, event.location, event.capacity, event.category])


def update_event_csv(updated_event: EventSchema):
    """
    Atualiza os dados de um evento existente no arquivo CSV.
    Se o evento com o ID correspondente for encontrado, ele será substituído pelos dados atualizados.
    """
    events = read_events()  # Lê todos os eventos no CSV
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)  # Reescreve o cabeçalho
        for event in events:  # Itera sobre os eventos
            # Substitui o evento correspondente pelo evento atualizado
            if event.id == updated_event.id:
                event = updated_event
            # Escreve o evento no arquivo
            writer.writerow([event.id, event.title, event.date, event.location, event.capacity, event.category])


def delete_event_csv(event_id: UUID):
    """
    Remove um evento do arquivo CSV com base no ID fornecido.
    Se o evento não for encontrado, lança uma exceção HTTP.
    """
    events = read_events()  # Lê todos os eventos no CSV
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)  # Reescreve o cabeçalho
        event_found = False  # Flag para verificar se o evento foi encontrado
        for event in events:
            if event.id == event_id:
                event_found = True  # Marca que o evento foi encontrado
                continue  # Pula a escrita desse evento, removendo-o
            # Escreve os eventos restantes no arquivo
            writer.writerow([event.id, event.title, event.date, event.location, event.capacity, event.category])
    if not event_found:  # Se nenhum evento com o ID fornecido foi encontrado
        raise HTTPException(status_code=404, detail="Event not found.")


def get_csv_hash() -> str:
    """
    Retorna o hash SHA256 do arquivo CSV para verificar sua integridade.
    """
    return generate_csv_hash(CSV_FILE)  # Função externa calcula o hash do arquivo


def compress_csv_file() -> str:
    """
    Compacta o arquivo CSV em um arquivo ZIP e retorna o caminho do arquivo compactado.
    """
    return zip_csv_file(CSV_FILE)  # Função externa realiza a compactação


def count_events() -> int:
    """
    Conta o número de eventos no arquivo CSV (excluindo o cabeçalho).
    """
    ensure_csv()  # Garante que o arquivo está configurado corretamente
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        return sum(1 for _ in file) - 1  # Conta todas as linhas e subtrai o cabeçalho
