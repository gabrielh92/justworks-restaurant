from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey
from uuid import uuid4

from src.models.restaurants import Restaurant
from src.models import Base

class Reservation(Base):
    __tablename__ = 'reservations'

    # Unique identifier
    uuid = Column(String, primary_key=True, default=uuid4())

    # Creation datetime of the reservation
    created_at = Column(DateTime, default=func.now())

    # Identifier for the restaurant in which the reservation is at
    restaurant_uuid = Column(ForeignKey(Restaurant.uuid))

    # Reservation details
    res_name = Column(String)
    res_date = Column(Date)
    res_slot = Column(String)
    res_size = Column(Integer)

    # Contact info
    phone = Column(String)
    email = Column(String)

    @classmethod
    async def get(cls):
        return

    @classmethod
    async def create(cls):
        return

    def __repr__(self):
        return f"<Reservation(id='{self.uuid}', restaurant='{self.restaurant_uuid}', name='{self.res_name}', date='{self.date}', slot='{self.slot}', party_size='{self.res_size}', phone={self.phone}, email={self.email})>"
