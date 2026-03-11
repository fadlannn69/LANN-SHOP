from fastapi import APIRouter,Query
from models.barang import Barang,Jenis
from config.dbbarang import collection
from bson import ObjectId
from typing import List
from schemas.barang import serialList,serialDict
import json

barang = APIRouter()


# mengambil file json
@barang.get("/",response_model=List[Barang])
async def find_barang(Jenis : Jenis = Query(...)):
    data = await (collection.find({"Jenis" : Jenis.value})).to_list(length=100)
    return serialList(data)
# mengambil file json

# membuat file json 
@barang.post("/")
async def create_user(barang: Barang):
    barang_dict = barang.model_dump()  
    result = await collection.insert_one(barang_dict)  
    
    barangs = await collection.find().to_list(length=100)
    barang_json = serialList(barangs)

    with open("barang.json", "w") as file:
        json.dump(barang_json, file, indent=4)

    return barang_json
# membuat file json

# mengedit file json
@barang.put("/{id}")
async def update_barang(id,barang : Barang):
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set" : dict(barang)})
    return serialDict(collection.find_one({"_id":ObjectId(id)}))
# mengedit file json

# menghapus file json
@barang.delete("/{id}")
async def delete_barang(id,barang : Barang):
    data = await collection.find_one_and_delete({"_id": ObjectId(id)}) 
    if data:
        return serialDict(data) 
# menghapus file json
