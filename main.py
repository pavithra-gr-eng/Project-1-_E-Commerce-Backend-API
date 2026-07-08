import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine

# Import models so SQLAlchemy creates the tables
from app.models import *

# Import routers
from app.routers.auth import router as auth_router
from app.routers.category import router as category_router
from app.routers.product import router as product_router
from app.routers.cart import router as cart_router
from app.routers.order import router as order_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Backend API",
    version="1.0.0",
    description="A production-ready E-Commerce Backend built with FastAPI.",
)
os.makedirs("uploads", exist_ok=True)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)

# Register routers
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the E-Commerce Backend API",
        "docs": "/docs",
        "redoc": "/redoc",
    }