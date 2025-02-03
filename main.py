from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
import mysql.connector
from sqlalchemy.orm import sessionmaker
from fastapi.responses import JSONResponse
import aiomysql
from mysql.connector import Error
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_201_CREATED
from fastapi.middleware.cors import CORSMiddleware
from databasee import Base,engine,SessionLocal

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="snehal@19",
        database="snehal",
    )


class User(BaseModel):
    name: str
    email: str
    password: str


class Order(BaseModel):
    user_id: int
    country_id: int
    parcel_size: int
    parcel_weight: float
    item_type: str
    banned_items: str # {“alcohol”, “drugs”, “Weapons”}
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/register/")
async def register_user(user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (user.name, user.email, user.password))
    connection.commit()
    cursor.close()
    connection.close()
    return connection

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An error occurred: {exc}"},
    )
@app.post("/create_order/")
async def create_order(order: Order, banned_items=[]):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Fetch the country details
    cursor.execute("SELECT max_size, max_weight, custom_duty_tax FROM countries WHERE country_id = %s",
                   (order.country_id,))
    country = cursor.fetchone()
    if not country:raise HTTPException(status_code=404, detail="Country not found")
    max_size, max_weight, custom_duty_tax = country
# Check if the parcel exceeds the max size or weight for the country
    if order.parcel_size > max_size or order.parcel_weight > max_weight:raise HTTPException(status_code=400, detail="Parcel exceeds size or weight limit")
# check Banned items
    #if order.parsel.item_type in banned_items: return {“MessageError”:“Item is banned in the destination country”}
# Calculate the shipping charge (for simplicity, let's assume a fixed charge per kg and size)
    shipping_charge = order.parcel_weight * 0.5 + order.parcel_size * 0.2 + custom_duty_tax
    cursor.execute("INSERT INTO orders (user_id, country_id, parcel_size, parcel_weight, shipping_charge) VALUES (%s, %s, %s, %s, %s)",
    (order.user_id, order.country_id, order.parcel_size, order.parcel_weight, shipping_charge))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Order created successfully", "shipping_charge": shipping_charge}
