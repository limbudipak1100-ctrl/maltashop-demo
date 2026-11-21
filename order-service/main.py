
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(
    title="MaltaShop Order Service",
    description="Manages customer orders",
    version="1.0.0"
)

# Temporary storage for prototype orders
orders = []

class Order(BaseModel):
    customer_id: str
    product_name: str
    quantity: int
    price: float

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/orders")
def create_order(order: Order):
    if order.quantity <= 0 or order.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity and price must be positive"
        )

    new_order = {
        "order_id": str(uuid4()),
        "customer_id": order.customer_id,
        "product_name": order.product_name,
        "quantity": order.quantity,
        "total": order.quantity * order.price,
        "status": "created"
    }

    orders.append(new_order)

    return new_order

@app.get("/orders")
def get_orders():
    return orders
