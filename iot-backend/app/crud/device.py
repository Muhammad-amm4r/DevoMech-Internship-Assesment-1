# app/crud/device.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.device import Device
from app.schemas.device import UserCreate, DeviceCreate, DeviceUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_in: UserCreate):
    hashed = pwd_ctx.hash(user_in.password)
    user = User(name=user_in.name, email=user_in.email, pwd_hash=hashed)
    db.add(user); db.commit(); db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email==email).first()

async def get_device(db: AsyncSession, device_id: int):
    result = await db.execute(select(Device).filter(Device.id == device_id))
    return result.scalar_one_or_none()

async def get_device_by_name(db: AsyncSession, name: str, user_id: int):
    result = await db.execute(
        select(Device).filter(Device.name == name, Device.user_id == user_id)
    )
    return result.scalar_one_or_none()

async def get_user_devices(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Device)
        .filter(Device.user_id == user_id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

async def create_device(db: AsyncSession, device: DeviceCreate, user_id: int):
    db_device = Device(
        name=device.name,
        location=device.location,
        status=device.status,
        user_id=user_id
    )
    db.add(db_device)
    await db.commit()
    await db.refresh(db_device)
    return db_device

async def update_device(
    db: AsyncSession, device_id: int, device_update: DeviceUpdate
):
    db_device = await get_device(db, device_id)
    if db_device:
        update_data = device_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_device, field, value)
        await db.commit()
        await db.refresh(db_device)
    return db_device

async def delete_device(db: AsyncSession, device_id: int):
    db_device = await get_device(db, device_id)
    if db_device:
        await db.delete(db_device)
        await db.commit()
    return db_device
