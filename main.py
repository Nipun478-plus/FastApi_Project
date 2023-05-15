from fastapi import FastAPI
from schemas.empolyee import empolyee
from config.db import con
from models.index import empolyees
app = FastAPI()


@app.get("/api/empolyees")
async def index():
    data=con.execute(empolyees.select()).fetchall()
    return {
        "success": True,
        "data":data
    }


@app.post("/api/empolyees")
async def store(empolyee:empolyee):
    data = con.execute(empolyees.insert().values(
        name = empolyee.name,
        email = empolyee.email,
        age = empolyee.age,
        country = empolyee.country,
        position = empolyee.position,
        salary = empolyee.salary,
       ))
    if data.is_insert:
        return {
            "success": True,
            "msg":"empolyee Store Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

@app.patch('/api/empolyees/{id}')
async def edit_data(id:int):
    data=con.execute(empolyees.select().where(empolyees.c.id==id)).fetchall()
    return {
        "success": True,
        "data":data
    }

# update data

@app.put('/api/empolyees/{id}')
async def update(id:int,empolyee:empolyee):
    data=con.execute(empolyees.update().values(
        name=empolyee.name,
        email=empolyee.email,
        age=empolyee.age,
        country=empolyee.country,
        position = empolyee.position,
        salary = empolyee.salary,
    ).where(empolyees.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"empolyee Update Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# delete data
@app.delete('/api/empolyees/{id}')
async def delete(id:int):
    data=con.execute(empolyees.delete().where(empolyees.c.id==id))
    if data:
        return {
            "success": True,
            "msg":"empolyee Delete Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# search data

@app.get('/api/empolyees/{search}')
async def search(search):
    data=con.execute(empolyees.select().where(empolyees.c.name.like('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data":data
    }