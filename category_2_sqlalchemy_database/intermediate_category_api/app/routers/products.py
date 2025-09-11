from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.deps import get_db
from app.crud import ProductCRUD


router = APIRouter(prefix="/products", tags=["Products"])


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = ProductCRUD(db).create_product(product)
    return db_product


@router.get(
    "/",
    response_model=List[ProductResponse],
    status_code=status.HTTP_200_OK,
)
def get_products(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    db_products = ProductCRUD(db).get_products(skip, limit)
    return db_products


@router.get(
    "/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK
)
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = ProductCRUD(db).get_product(id)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found !"
        )
    return db_product


@router.put(
    "/{id}",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def update_product(
    id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    db_product = ProductCRUD(db).update_product(id, product)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return db_product


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = ProductCRUD(db).delete_product(id)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
