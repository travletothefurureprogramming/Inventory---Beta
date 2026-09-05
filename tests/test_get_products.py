from app.services.product_service import get_products


products = get_products()

print(f"Total products: {len(products)}")

for product in products:
    print(
        f"ID: {product.id} | "
        f"Name: {product.name} | "
        f"SKU: {product.sku} | "
        f"Stock: {product.stock}"
    )