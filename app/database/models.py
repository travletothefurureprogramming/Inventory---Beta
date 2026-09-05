from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(200), nullable=False)

    sku: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    barcode: Mapped[str | None] = mapped_column(String(100), nullable=True)

    category: Mapped[str | None] = mapped_column(String(100), nullable=True)

    purchase_price: Mapped[float] = mapped_column(Float, nullable=False)

    selling_price: Mapped[float] = mapped_column(Float, nullable=False)

    vat: Mapped[float] = mapped_column(Float, default=24.0)

    stock: Mapped[int] = mapped_column(Integer, default=0)

    minimum_stock: Mapped[int] = mapped_column(Integer, default=0)