from fastapi import APIRouter,BackgroundTasks
from models.pesan import Pesanan
from config.dbpesanan import collection
from bson import ObjectId
from typing import List
from schemas.pesan import serialList
import json
# email
from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from pydantic import BaseModel,EmailStr
import os
from dotenv import load_dotenv
pesanan = APIRouter()

load_dotenv()
print(os.getenv("lanntikshop@gmail.com"))
# model
class EmailSchema(BaseModel):
    email : EmailStr
    subject : str
    content : str

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)
async def send_email(email: EmailSchema):
    message = MessageSchema(
        subject=email.subject,
        recipients=[email.email],
        body=email.content,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
# endpoint email
@pesanan.post("/send-email/")
async def send_email_api(email:EmailSchema,background_task : BackgroundTasks):
    background_task.add_task(send_email,email)
    return {"message":f"Email dikirim ke {email.email}"}

# mengambil file json
@pesanan.get("/")
async def find_barang():
    data = await (collection.find()).to_list(length=100)
    return serialList(data)
# mengambil file json

# membuat file json 
@pesanan.post("/")
async def create_pesan(pesanan: Pesanan):
    barang_dict = pesanan.model_dump()  
    result = await collection.insert_one(barang_dict)  
    
    barangs = await collection.find().to_list(length=100)
    barang_json = serialList(barangs)

    with open("pesanan.json", "w") as file:
        json.dump(barang_json, file, indent=4)

    return barang_json
# membuat file json

@pesanan.delete("/")
async def delete_barang():
    data = await collection.delete_many({}) 
    return {"jumlah_delet" : data.deleted_count} 


