from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class TelemetryBase(BaseModel):
    temperature: Optional[float] = None
    battery_level: Optional[float] = None
    data: Optional[Dict[str, Any]] = None

class TelemetryCreate(TelemetryBase):
    device_id: int

class Telemetry(TelemetryBase):
    id: int
    device_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class DeviceLatestStatus(BaseModel):
    device_id: int
    device_name: str
    last_online: Optional[datetime] = None
    status: str
    latest_telemetry: Optional[Telemetry] = None

    class Config:
        from_attributes = True 