from app.services.product_service import delete_product


result = delete_product(2)

if result:
    print("Product deleted successfully!")
else:
    print("Product not found!")