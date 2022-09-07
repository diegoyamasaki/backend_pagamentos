from fastapi import APIRouter
from interface.home.home_interface import home_router

routes = APIRouter()

routes.include_router(home_router, prefix="", tags=["home"])
