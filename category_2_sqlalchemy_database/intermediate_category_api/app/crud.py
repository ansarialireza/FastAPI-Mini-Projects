from sqlalchemy.orm import Session, joinedload
from app import schemas, models


class CategoryCRUD:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_category(self, category: schemas.CategoryCreate):
        db_category = models.Category(**category.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_categories(self, skip: int, limit: int):
        return (
            self.db.query(models.Category)
            .options(joinedload(models.Category.products))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_category(self, id: int):
        return (
            self.db.query(models.Category)
            .filter(models.Category.id == id)
            .one_or_none()
        )

    def update_category(self, id: int, category: schemas.CategoryUpdate):
        db_category = self.get_category(id)
        if db_category is None:
            return None
        for key, value in category.model_dump(exclude_unset=True).items():
            setattr(db_category, key, value)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def delete_category(self, id: int):
        db_category = self.get_category(id)
        if db_category is None:
            return None
        self.db.delete(db_category)
        self.db.commit()
        return db_category


class ProductCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: schemas.ProductCreate):
        db_product = models.Product(**product.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_products(self, skip: int, limit: int):
        return (
            self.db.query(models.Product)
            .options(joinedload(models.Product.category))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_product(self, id: int):
        return (
            self.db.query(models.Product)
            .filter(models.Product.id == id)
            .one_or_none()
        )

    def update_product(self, id: int, product: schemas.ProductUpdate):
        db_product = self.get_product(id)
        if db_product is None:
            return None
        for key, value in product.model_dump(exclude_unset=True).items():
            setattr(db_product, key, value)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete_product(self, id: int):
        db_product = self.get_product(id)
        if db_product is None:
            return None
        self.db.delete(db_product)
        self.db.commit()
        return db_product
