from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DeviceBase(BaseModel):
    name: str
    location: Optional[str] = None
    status: Optional[str] = "offline"

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None

class Device(DeviceBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True 