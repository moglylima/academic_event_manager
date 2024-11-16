from fastapi import FastAPI
from app.api.endpoints import events

app = FastAPI()

# Incluindo as rotas
app.include_router(events.router, prefix="/events", tags=["events"])

@app.get("/")
def root():
    return {"message": "Welcome to the Events API"}
