from uuid import uuid4
from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.sql import func
from src.models import Base, engine

class Restaurant(Base):
    __tablename__ = "restaurants"

    # Unique identifier for the restaurant
    uuid = Column(String, primary_key=True, default=uuid4())

    # Time the restaurant was registered in the system
    created_at = Column(DateTime, default=func.now())

    # Restaurant name
    name = Column(String)

    # Full address of the restaurant
    # Could be sanitized and parsed to split into street address, city, state and zip (for U.S.)
    address = Column(String)

    # This could potentially be more nuanced to account for party size restrictions,
    # specific capacity tables vs flexible seating (tables that can be moved), etc
    # Using as a simple int representing maximum capacity of the restaurant until we have more detailed reqs
    capacity = Column(Integer)
