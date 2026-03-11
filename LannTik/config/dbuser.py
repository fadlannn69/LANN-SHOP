# from pymongo import MongoClient
import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://username:password@localhost:27017")
db = client["local"]
collection = db["user"]