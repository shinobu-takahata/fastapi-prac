"""
routes
"""

from fastapi import FastAPI
from routers import item as item_route

app = FastAPI()
app.include_router(item_route.router)
