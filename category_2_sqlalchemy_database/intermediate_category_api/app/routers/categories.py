from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app.deps import get_db
from app.crud import CategoryCRUD

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(
    "/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED
)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = CategoryCRUD(db).create_category(category)
    return db_category


@router.get(
    "/", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK
)
def get_categories(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    db_categories = CategoryCRUD(db).get_categories(skip, limit)
    return db_categories


@router.get(
    "/{id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK
)
def get_category(id: int, db: Session = Depends(get_db)):
    db_category = CategoryCRUD(db).get_category(id)
    print(db_category)
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    return db_category


@router.put(
    "/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED
)
def update_category(
    id: int, category: CategoryUpdate, db: Session = Depends(get_db)
):
    db_category = CategoryCRUD(db).update_category(id, category)
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    return db_category


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id: int, db: Session = Depends(get_db)):
    category = CategoryCRUD(db).delete_category(id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
