from sqlalchemy import select
from app.database.database import SessionLocal
from app.database.models import Product

session = SessionLocal()

result = session.execute(select(Product))

products = result.scalars().all()

for product in products:
    print(product.name)
    print(product.sku)
    print(product.stock)
    print("----------------")

session.close()