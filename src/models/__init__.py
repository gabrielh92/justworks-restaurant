from fastapi.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker

import logging
import os

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M')

# This is not done within a try/catch because we want it throw if it fails
# and cause server startup to fail
db_url = os.environ.get('DATABASE_URL')
engine = create_engine(db_url, echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
logger.info(f"Created session for database: '{db_url}'")

# Used to prepopulate the database with some testing data
def seed():
    logger.info("Seeding database")

    # Create tables
    from src.models.restaurants import Restaurant
    from src.models.reservations import Reservation
    Base.registry.configure()
    Base.metadata.create_all(engine)

    restaurant = Restaurant(name="Gabriel's", address="123 Bushwick Ave, Brooklyn NY 11206", capacity=20)

    with Session() as session:
        res = session.query(Restaurant).filter_by(name="Gabriel's").first()
        if not res:
            session.add(restaurant)
            session.commit()
        else:
            logger.info("Skipping test restaurant entries since already present")

    logger.info("DONE!")
