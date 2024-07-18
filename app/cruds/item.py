"""
This module defines the Item and ItemStatus classes for representing items
in an inventory system.
"""

from enum import Enum
from typing import Optional


class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


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


def create(item_create):
    new_item = Item(
        id=len(items) + 1,
        name=item_create.get("name"),
        price=item_create.get("price"),
        description=item_create.get("description"),
        status=ItemStatus.ON_SALE,
    )
    items.append(new_item)
    return new_item


def update(item_id: int, item_update: dict):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = Item(
                id=item_id,
                name=item_update.get("name", item.name),
                price=item_update.get("price", item.price),
                description=item_update.get("description", item.description),
                status=item_update.get("status", item.status),
            )
            return items[index]
    return None


def delete(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return True
    return False
