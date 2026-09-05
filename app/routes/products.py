from fastapi import APIRouter, HTTPException

from app.services.product_service import get_products, get_product_by_id, add_product, Product, update_product, delete_product
from app.schemas.products import ProductResponse, ProductCreate, ProductUpdate


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def read_products():
    products = get_products()

    return products

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):

    new_product = Product(
        name=product.name,
        sku=product.sku,
        barcode=product.barcode,
        category=product.category,
        purchase_price=product.purchase_price,
        selling_price=product.selling_price,
        vat=product.vat,
        stock=product.stock,
        minimum_stock=product.minimum_stock
    )

    created_product = add_product(new_product)

    if created_product is None:
        raise HTTPException(
            status_code=409,
            detail="A product with this SKU already exists."
        )

    return created_product

@router.put("/{id}", response_model=ProductResponse)
def edit_product(id: int, product: ProductUpdate):
    updated_product = update_product(id, product.stock)

    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product


@router.delete("/{id}")
def remove_product(id: int):
    deleted = delete_product(id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {"message": "Product deleted successfully"}