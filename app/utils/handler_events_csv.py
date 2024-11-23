# Todas as operações no CSV -> Create, Read, Update, Delete (CRUD)

# Funcoes para serem implementadas, chamadas em outros arquivos
import csv
from models.event import Event

class events_handler_csv:
    # Construtor, sempre será criado um objeto dessa classe com o caminho do arquivo
     def __init__(self, file_path: str):
        self.file_path = file_path
        
    def create_event(self, event: Event):
        
        
    def get_all_events(self):
        
    
    def get_event(self, event_id: int):
        
    
    def update_event(self, event_id: int, updated_event: Event):
        
        
    def delete_event(self, event_id: int):
        
    
    def read_events(self):
        
    def zip_events(self):
        
    def hash_file_events(self):
            