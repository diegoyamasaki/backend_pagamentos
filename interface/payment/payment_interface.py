from fastapi import APIRouter
from domain.entities.payment import Payment

payment_router = APIRouter(prefix="/boletos")


@payment_router.post("/bancarios")
async def pagamentos_bancarios(payment: Payment):
    return {"msg": "pagamentos bancarios"}


@payment_router.post("/consumo")
async def pagamentos_de_consumo(payment: Payment):
    return {"msg": "pagamentos de consumo"}

