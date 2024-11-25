from fastapi import FastAPI
from app.routes.event_router import router as event_router

app = FastAPI()

# Incluindo as rotas
app.include_router(event_router, prefix="/api/v1")
