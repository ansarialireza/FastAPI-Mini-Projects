from fastapi import FastAPI
from simple_product_api import models, database
from simple_product_api.routers import products, categories

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(categories.router)
