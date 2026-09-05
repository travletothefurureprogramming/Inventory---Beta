from app.services.product_service import get_product_by_id


product = get_product_by_id(1)

if product:
    print("Product found!")
    print(f"ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"SKU: {product.sku}")
    print(f"Stock: {product.stock}")
else:
    print("Product not found!")