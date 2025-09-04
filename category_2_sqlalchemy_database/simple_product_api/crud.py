from sqlalchemy.orm import Session
from simple_product_api import models, schemas


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return (
        db.query(models.Category)
        .filter(models.Category.id == category_id)
        .one_or_none()
    )


def update_category(
    db: Session, category_id: int, category: schemas.CategoryUpdate
):
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )


def update_product(
    db: Session, product_id: int, product: schemas.ProductUpdate
):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
