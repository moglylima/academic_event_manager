from fastapi import FastAPI
from app.routes.event_router import router as event_router

app = FastAPI(
    title="Academic Event Manager",
    description="API to manage academic events. Provides full CRUD operations, event counting, CSV file compression, and SHA256 hash calculation.",
    version="1.0.0",
    contact={
        "name": "Development Team",
        "email": "moglesonlima@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Including routes
app.include_router(event_router, prefix="/api/v1")
