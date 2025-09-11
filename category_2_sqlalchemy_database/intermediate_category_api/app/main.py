from fastapi import FastAPI
from app import models, database
from app.routers import products, categories

models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.include_router(products.router)
app.include_router(categories.router)
