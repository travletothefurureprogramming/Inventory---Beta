from app.database.models import Product
from app.services.product_service import add_product


product = Product(
    name="Raspberry Pi 5",
    sku="RPI5-001",
    barcode="123456789012",
    category="Computers",
    purchase_price=60.0,
    selling_price=79.99,
    vat=24.0,
    stock=5,
    minimum_stock=2
)


result = add_product(product)


if result:
    print("Product added successfully!")
    print(f"ID: {result.id}")
    print(f"Name: {result.name}")
    print(f"SKU: {result.sku}")
else:
    print("Product already exists!")