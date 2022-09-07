from fastapi import APIRouter
from interface.home.home_interface import home_router
from interface.payment.payment_interface import payment_router

routes = APIRouter()

routes.include_router(home_router, prefix="", tags=["home"])
routes.include_router(payment_router, prefix="/pagamentos", tags=["pagamentos"])
