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