from fastapi import FastAPI
from routes.user import user
from routes.barang import barang
from routes.pesan import pesanan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user , prefix="/user" , tags=["User"])
app.include_router(barang , prefix="/Barang" , tags=["Barang"])
app.include_router(pesanan , prefix="/Pesanan" , tags=["Pesanan"])
