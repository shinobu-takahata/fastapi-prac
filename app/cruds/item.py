"""
This module defines the Item and ItemStatus classes for representing items
in an inventory system.
"""

from typing import Optional
from schemas.schemas import ItemCreate, ItemStatus, ItemUpdate


class Item:

    def __init__(
        self,
        id: int,
        name: str,
        price: int,
        description: Optional[str],
        status: ItemStatus,
    ) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status


items = [
    Item(1, "Item 1", 10, "Description 1", ItemStatus.ON_SALE),
    Item(2, "Item 2", 20, "Description 2", ItemStatus.SOLD_OUT),
    Item(3, "Item 3", 30, "Description 3", ItemStatus.ON_SALE),
]


def find_all():
    return items


def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None


def find_by_name(name: str):
    filtered_name = []
    for item in items:
        if name in item.name:
            filtered_name.append(item)
    return filtered_name


def create(item_create: ItemCreate):
    new_item = Item(
        id=len(items) + 1,
        name=item_create.name,
        price=item_create.price,
        description=item_create.description,
        status=ItemStatus.ON_SALE,
    )
    items.append(new_item)
    return new_item


def update(item_id: int, item_update: ItemUpdate):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = Item(
                id=item_id,
                name=item.name if item_update.name is None else item_update.name,
                price=item.price if item_update.price is None else item_update.price,
                description=(
                    item.description
                    if item_update.description is None
                    else item_update.description
                ),
                status=(
                    item.status if item_update.status is None else item_update.status
                ),
            )
            return items[index]
    return None


def delete(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    return None
