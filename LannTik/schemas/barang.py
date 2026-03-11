
# barang entity
def barangEntity(items) -> dict:
    return{
        "id":str(items["_id"]),
        "Nama":items["Nama"],
        "Gambar":items["Gambar"],
    }

def barangsEntity(entitas) -> list:
    return [barangsEntity(items)for items in entitas]

def serialDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=="_id"},**{i:(a[i]) for i in a if i!="_id"}}

def serialList(entitas) -> list:
    return [serialDict(a)for a in entitas]

