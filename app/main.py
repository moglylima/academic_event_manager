from fastapi import FastAPI
from app.api.endpoints import event_router

app = FastAPI()

# Incluindo as rotas
app.include_router(event_router.router, prefix="/events", tags=["events"])

@app.get("/")
def root():
    return {"message": "Welcome to the Events API"}
