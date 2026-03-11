from pydantic import BaseModel

    
class Pesanan(BaseModel):
    Nama : str
    Harga : int