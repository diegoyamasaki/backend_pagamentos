from fastapi import APIRouter
from interface.home.home_interface import home_router
from interface.payment.payment_interface import billet_payment_router

routes = APIRouter()

routes.include_router(home_router, prefix="", tags=["Health Check"])
routes.include_router(billet_payment_router, prefix="/pagamentos", tags=["Boletos"])
