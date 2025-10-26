from motor.motor_asyncio import AsyncIOMotorClient

# Local MongoDB URI
MONGO_URI = "mongodb://localhost:27017"

# Create client
client = AsyncIOMotorClient(MONGO_URI)

# Select database
db = client["vibely"]

# Select collection
user_collection = db["users"]
