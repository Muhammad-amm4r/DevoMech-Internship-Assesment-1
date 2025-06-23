from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

# Create a base class for declarative models
Base = declarative_base()

# expose metadata for migrations
metadata = Base.metadata

# Import all models here for Alembic to detect
from app.models.user import User  # noqa
from app.models.device import Device  # noqa
from app.models.telemetry import Telemetry  # noqa
