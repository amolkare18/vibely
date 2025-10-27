# models.py
from db import db

# Reference to the users collection
user_collection = db["users"]

# Function to create a user in MongoDB
async def create_user_db(user_data: dict) -> str:
    result = await user_collection.insert_one(user_data)
    return str(result.inserted_id)

