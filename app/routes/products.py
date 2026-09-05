from fastapi import APIRouter

from app.services.product_service import get_products
from app.schemas.products import ProductResponse


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def read_products():
    products = get_products()

    return products

