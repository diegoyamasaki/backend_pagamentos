from fastapi import APIRouter
from domain.entities.billet_payment import BilletPayment

billet_payment_router = APIRouter(prefix="/boletos")


@billet_payment_router.post("/bancario")
async def pagamento_de_boletos_bancarios(billet_payment: BilletPayment):
    return {"msg": "pagamentos bancarios"}


@billet_payment_router.post("/consumo")
async def pagamento_de_boletos_de_consumo(billet_payment: BilletPayment):
    return {"msg": "pagamentos de consumo"}

