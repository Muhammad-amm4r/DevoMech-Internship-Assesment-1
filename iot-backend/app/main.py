from fastapi import FastAPI
from app.api import auth, users, devices, telemetry
from app.db.session import engine
from app.db.base import metadata

app = FastAPI(title="IoT Backend")

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

app.include_router(auth.router)
app.include_router(users.router, prefix="/users")
app.include_router(devices.router, prefix="/devices")
app.include_router(telemetry.router, prefix="/telemetry")
