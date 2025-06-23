from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Specific telemetry fields
    temperature = Column(Float, nullable=True)
    battery_level = Column(Float, nullable=True)
    
    # Generic JSON data for additional telemetry
    data = Column(JSON, nullable=True)
    
    # Relationships
    device = relationship("Device", back_populates="telemetry")
