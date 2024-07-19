from fastapi import APIRouter, Path, Query
from cruds import item
from schemas.schemas import ItemCreate, ItemResponse, ItemUpdate
from fastapi import HTTPException


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=list[ItemResponse])
async def find_all():
    return item.find_all()


@router.get("/{item_id}", response_model=ItemResponse)
async def find_by_id(item_id: int = Path(gt=0)):
    found_item = item.find_by_id(item_id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item


@router.get("/", response_model=list[ItemResponse])
async def find_by_name(name: str = Query(min_length=2, max_length=20)):
    return item.find_by_name(name)


@router.post("", response_model=ItemResponse)
async def create(item_create: ItemCreate):
    return item.create(item_create)


@router.put("/{item_id}", response_model=ItemResponse)
async def update(item_update: ItemUpdate, item_id: int = Path(gt=0)):
    updated_item = item.update(item_id, item_update)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}", response_model=ItemResponse)
async def delete(item_id: int = Path(gt=0)):
    deleted_item = item.delete(item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item
