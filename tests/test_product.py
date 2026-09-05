from sqlalchemy import select
from app.database.database import SessionLocal
from app.database.models import Product

session = SessionLocal()

product = Product(
    name="Arduino Uno",
    sku="ARD-UNO-001",
    barcode="123456789",
    category="Electronics",
    purchase_price=20.0,
    selling_price=29.99,
    vat=24.0,
    stock=10,
    minimum_stock=2
)

session.add(product)

session.commit()

print(f"Product saved with ID: {product.id}")



session.close()