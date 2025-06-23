# app/crud/user.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_in: UserCreate):
    hashed = pwd_ctx.hash(user_in.password)
    user = User(name=user_in.name, email=user_in.email, pwd_hash=hashed)
    db.add(user); db.commit(); db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email==email).first()

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List

from app.models.telemetry import Telemetry
from app.schemas.telemetry import TelemetryCreate

async def create_telemetry(db: AsyncSession, telemetry: TelemetryCreate):
    db_telemetry = Telemetry(
        device_id=telemetry.device_id,
        temperature=telemetry.temperature,
        battery_level=telemetry.battery_level,
        data=telemetry.data
    )
    db.add(db_telemetry)
    await db.commit()
    await db.refresh(db_telemetry)
    return db_telemetry

async def get_device_telemetry(
    db: AsyncSession, device_id: int, skip: int = 0, limit: int = 100
) -> List[Telemetry]:
    result = await db.execute(
        select(Telemetry)
        .filter(Telemetry.device_id == device_id)
        .order_by(desc(Telemetry.timestamp))
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

async def get_latest_telemetry(db: AsyncSession, device_id: int) -> Optional[Telemetry]:
    result = await db.execute(
        select(Telemetry)
        .filter(Telemetry.device_id == device_id)
        .order_by(desc(Telemetry.timestamp))
        .limit(1)
    )
    return result.scalar_one_or_none()
