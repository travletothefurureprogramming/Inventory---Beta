from sqlalchemy import create_engine

from .models import Base

DATABASE = "sqlite:///data/inventory.db"

engine = create_engine(
    DATABASE,
    echo=True
)


def create_database():
    Base.metadata.create_all(engine)