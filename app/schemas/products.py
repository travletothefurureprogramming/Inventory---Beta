from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str

    sku: str

    barcode: str | None = None

    category: str | None = None

    purchase_price: float

    selling_price: float

    vat: float

    stock: int

    minimum_stock: int

class ProductUpdate(BaseModel):

    stock: int

class ProductResponse(BaseModel):
    id: int

    name: str

    sku: str

    barcode: str | None = None

    category: str | None = None

    purchase_price: float

    selling_price: float

    vat: float

    stock: int

    minimum_stock: int