from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models import Product


def add_product(product: Product):
    session = SessionLocal()

    result = session.execute(
        select(Product).where(Product.sku == product.sku)
    )

    existing_product = result.scalar_one_or_none()

    if existing_product is not None:
        session.close()
        return None

    session.add(product)
    session.commit()
    session.refresh(product)

    session.close()

    return product

def get_product_by_id(product_id: int):
    session = SessionLocal()

    product = session.get(Product, product_id)

    session.close()

    return product


def get_products():
    session = SessionLocal()

    result = session.execute(
        select(Product)
    )

    products = result.scalars().all()

    session.close()

    return products


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


def delete_product(product_id: int):
    session = SessionLocal()

    product = session.get(Product, product_id)

    if product is None:
        session.close()
        return False

    session.delete(product)
    session.commit()

    session.close()

    return True