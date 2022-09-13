from fastapi import APIRouter
from domain.schemas.bank_payment import BankPayment
from domain.schemas.consumer_payment import ConsumerPayment

billet_payment_router = APIRouter(prefix="/boletos")


@billet_payment_router.post("/bancario")
async def pagamento_de_boletos_bancarios(payment: BankPayment):
    return {"msg": "pagamentos bancarios"}


@billet_payment_router.post("/consumo")
async def pagamento_de_boletos_de_consumo(payment: ConsumerPayment):
    return {"msg": "pagamentos de consumo"}

