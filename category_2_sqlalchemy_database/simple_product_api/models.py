from sqlalchemy import Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional, List
from datetime import datetime
from simple_product_api.database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="category", cascade="all, delete-orphan"
    )


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )

    category: Mapped[Optional[Category]] = relationship(
        "Category", back_populates="products"
    )
