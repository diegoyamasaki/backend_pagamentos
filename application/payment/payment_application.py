from sqlalchemy.orm import Session
from domain.entities.bank_payment import BankPayment
from domain.entities.consumer_payment import ConsumerPayment


class PaymentApplication:

    def __init__(self, database: Session):

        self._db = database

    def make_payment_bank(self, payment: BankPayment) -> None:
        print("realiza pagamento boleto de banco")
        bank = BankPayment()
        bank.billet = payment.billet
        bank.amount = payment.amount
        self._db.add(bank)
        self._db.commit()
        self._db.refresh(bank)
        return bank

    def make_payment_consumer(self, payment: ConsumerPayment) -> None:
        print("realiza pagamento boleto de consumo")
        consumer = ConsumerPayment()
        consumer.amount = payment.amount
        consumer.billet = payment.billet
        self._db.add(consumer)
        self._db.commit()
        self._db.refresh(consumer)
        return consumer
