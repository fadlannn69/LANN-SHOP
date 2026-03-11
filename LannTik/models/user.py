from pydantic import BaseModel,EmailStr

class User(BaseModel):
    Nama : str
    Email : EmailStr
    Alamat : str
