from fastapi import APIRouter, Depends, status
from infra.database.conection import get_db
from sqlalchemy.orm import Session
from application.payment.payment_application import PaymentApplication
from domain.schemas.bank_payment import BankPayment
from domain.schemas.consumer_payment import ConsumerPayment

billet_payment_router = APIRouter(prefix="/boletos")


@billet_payment_router.post("/bancario", status_code=status.HTTP_201_CREATED)
async def pagamento_de_boletos_bancarios(payment: BankPayment,
                                         db: Session = Depends(get_db)):
    application = PaymentApplication(db)
    return application.make_payment_bank(payment)


@billet_payment_router.post("/consumo", status_code=status.HTTP_201_CREATED)
async def pagamento_de_boletos_de_consumo(payment: ConsumerPayment,
                                          db: Session = Depends(get_db)):
    application = PaymentApplication(db)
    return application.make_payment_consumer(payment)

