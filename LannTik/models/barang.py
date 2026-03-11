from pydantic import BaseModel
from enum import Enum
class Jenis(str,Enum):
    def __str__(self):
        return self.value
    MicroController = "MicroController"
    Electrical = "Electrical"
    Sensor = "Sensor"
    
class Barang(BaseModel):
    Nama : str
    Jenis : Jenis
    Harga : int
    Gambar : str