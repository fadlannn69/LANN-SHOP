from fastapi import APIRouter
from models.user import User
from config.dbuser import collection
from schemas.user import serializeDict,serializeList
from bson import ObjectId
import json

user = APIRouter()


@user.get("/")
async def find_all_users():
    data = await (collection.find()).to_list(length=100) 
    return serializeList(data)

@user.post("/")
async def create_user(user: User):
    user_dict = user.model_dump()  
    result = await collection.insert_one(user_dict)  
    
    users = await collection.find().to_list(length=100)
    user_json = serializeList(users)

    with open("user.json", "w") as file:
        json.dump(user_json, file, indent=4)

    return user_json

@user.put("/{id}")
async def update_user(id,user : User):
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set" : dict(user)})
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@user.delete("/")
async def delete_barang():
    data = await collection.delete_many({}) 
    return {"jumlah_delet" : data.deleted_count} 




