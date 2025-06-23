from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_current_user, get_db
from app.crud.device import get_device
from app.crud.telemetry import (
    create_telemetry,
    get_device_telemetry,
    get_latest_telemetry,
)
from app.models.user import User
from app.schemas.telemetry import (
    Telemetry as TelemetrySchema,
    TelemetryCreate,
    DeviceLatestStatus,
)

router = APIRouter()

@router.post("/", response_model=TelemetrySchema)
async def create_telemetry_data(
    telemetry: TelemetryCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Check if the device exists and belongs to the user
    device = await get_device(db, telemetry.device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    
    return await create_telemetry(db, telemetry)

@router.get("/device/{device_id}", response_model=List[TelemetrySchema])
async def read_device_telemetry(
    device_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Check if the device exists and belongs to the user
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    
    return await get_device_telemetry(db, device_id, skip, limit)

@router.get("/device/{device_id}/latest", response_model=TelemetrySchema)
async def read_latest_telemetry(
    device_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Check if the device exists and belongs to the user
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    
    telemetry = await get_latest_telemetry(db, device_id)
    if telemetry is None:
        raise HTTPException(status_code=404, detail="No telemetry data found for this device")
    
    return telemetry

@router.get("/device/{device_id}/status", response_model=DeviceLatestStatus)
async def read_device_status(
    device_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Check if the device exists and belongs to the user
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    
    latest_telemetry = await get_latest_telemetry(db, device_id)
    
    return DeviceLatestStatus(
        device_id=device.id,
        device_name=device.name,
        status=device.status,
        last_online=latest_telemetry.timestamp if latest_telemetry else None,
        latest_telemetry=latest_telemetry,
    ) 