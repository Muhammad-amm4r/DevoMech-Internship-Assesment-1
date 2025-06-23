from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_current_user, get_db
from app.crud.device import (
    create_device,
    get_device,
    get_user_devices,
    update_device,
    delete_device,
)
from app.models.user import User
from app.schemas.device import Device as DeviceSchema, DeviceCreate, DeviceUpdate

router = APIRouter()

@router.post("/", response_model=DeviceSchema)
async def create_new_device(
    device: DeviceCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_device(db, device, current_user.id)

@router.get("/", response_model=List[DeviceSchema])
async def read_devices(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    devices = await get_user_devices(db, current_user.id, skip, limit)
    return devices

@router.get("/{device_id}", response_model=DeviceSchema)
async def read_device(
    device_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.put("/{device_id}", response_model=DeviceSchema)
async def update_device_endpoint(
    device_id: int,
    device_update: DeviceUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    return await update_device(db, device_id, device_update)

@router.delete("/{device_id}", response_model=DeviceSchema)
async def delete_device_endpoint(
    device_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    device = await get_device(db, device_id)
    if device is None or device.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Device not found")
    return await delete_device(db, device_id) 