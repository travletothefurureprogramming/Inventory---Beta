from sqlalchemy import create_engine, select 
from sqlalchemy.orm import sessionmaker

from .models import Base, Product

DATABASE = "sqlite:///data/inventory.db"

engine = create_engine(
    DATABASE,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def create_database():
    Base.metadata.create_all(engine)

def read_database():
    session = SessionLocal()
    result = session.execute(select(Product))

    products = result.scalars().all()

    session.close()

    return products


def create_product(instance: Product):
    session = SessionLocal()

    session.add(instance)
    session.commit()

    session.refresh(instance)

    session.close()

    return instance


def update_product(product_id: int, stock: int):
    session = SessionLocal()

    product = session.get(Product, product_id)

    if product is None:
        session.close()
        return None

    product.stock = stock

    session.commit()
    session.refresh(product)

    session.close()

    return product