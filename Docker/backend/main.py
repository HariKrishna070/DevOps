from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

# Environment variables or hardcoded credentials
MONGODB_USERNAME = os.getenv("MONGO_DB_USERNAME", "admin")  # Default to 'admin' if not found
MONGODB_PASSWORD = os.getenv("MONGO_DB_PASSWORD", "password")  # Default to 'password' if not found
MONGO_URI = os.getenv("MONGO_URI")

# Dependency to get a database connection per request
def get_db():
    try:
        print(f"Mongo uri : {MONGO_URI}")
        client = MongoClient(MONGO_URI)
        db = client["mydatabase"]
        collection = db["items"]
        yield collection  # Use `yield` for returning the collection lazily
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error : {str(e)}")
    finally:
        client.close()  # Close the client after request is done


class Item(BaseModel):
    id: int
    name: str
    description: str = ""


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}


@app.post("/items/", response_model=Item)
def create_item(item: Item, collection = Depends(get_db)):
    # Check if the item already exists
    if collection.find_one({"id": item.id}):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    collection.insert_one(item.dict())
    return item


@app.get("/items/", response_model=List[Item])
def get_items(collection = Depends(get_db)):
    items = list(collection.find({}, {'_id': 0}))  # Exclude Mongo's internal _id
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, collection = Depends(get_db)):
    item = collection.find_one({"id": item_id}, {'_id': 0})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item, collection = Depends(get_db)):
    result = collection.replace_one({"id": item_id}, updated_item.dict())
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int, collection = Depends(get_db)):
    result = collection.delete_one({"id": item_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
