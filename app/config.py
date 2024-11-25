import os

# Base directory do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho padrão para o arquivo CSV
CSV_FILE_PATH = os.path.join(BASE_DIR, "data/event.csv")

# Garante que o diretório de dados existe
os.makedirs(os.path.dirname(CSV_FILE_PATH), exist_ok=True)
