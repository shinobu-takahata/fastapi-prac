from fastapi import APIRouter

from cruds import item
from schemas.schemas import ItemCreate, ItemUpdate


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("")
async def find_all():
    return item.find_all()


@router.get("/{item_id}")
async def find_by_id(item_id: int):
    return item.find_by_id(item_id)


@router.get("/")
async def find_by_name(name: str):
    return item.find_by_name(name)


@router.post("")
async def create(item_create: ItemCreate):
    return item.create(item_create)


@router.put("/{item_id}")
async def update(item_id: int, item_update: ItemUpdate):
    return item.update(item_id, item_update)


@router.delete("/{item_id}")
async def delete(item_id: int):
    return item.delete(item_id)
