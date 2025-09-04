from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from simple_product_api import schemas, crud, database


router = APIRouter(prefix="/cetegories", tags=["Categories"])


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Category)
def create_category(
    category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_category(db, category)


@router.get("/", response_model=List[schemas.Category])
def read_categories(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return crud.get_categories(db, skip, limit)


@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    return db_category


@router.put("/{category_id}", response_model=schemas.CategoryUpdate)
def update_category(
    category_id: int,
    category: schemas.CategoryUpdate,
    db: Session = Depends(get_db),
):
    db_category = crud.update_category(db, category_id, category)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found."
        )
    return db_category


@router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db, category_id)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found."
        )
    return db_category
