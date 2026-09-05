from app.services.product_service import update_product


product = update_product(2, 8)

if product:
    print("Product updated successfully!")
    print(f"ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"SKU: {product.sku}")
    print(f"New stock: {product.stock}")
else:
    print("Product not found!")