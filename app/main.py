"""
routes
"""

from fastapi import Body, FastAPI

from cruds import item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
async def find_all():
    return item.find_all()


@app.get("/items/{item_id}")
async def find_by_id(item_id: int):
    return item.find_by_id(item_id)


@app.get("/items/")
async def find_by_name(name: str):
    return item.find_by_name(name)


@app.post("/items")
async def create(item_create: dict = Body(...)):
    return item.create(item_create)


@app.put("/items/{item_id}")
async def update(item_id: int, item_update: dict = Body(...)):
    return item.update(item_id, item_update)


@app.delete("/items/{item_id}")
async def delete(item_id: int):
    return item.delete(item_id)
