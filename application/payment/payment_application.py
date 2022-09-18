from sqlalchemy.orm import Session
from domain.entities.bank_payment import BankPayment
from domain.entities.consumer_payment import ConsumerPayment
from shared.notify import Notify
from shared.observer import Observer


class PaymentApplication(Notify):

    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

        

    def __init__(self, database: Session):

        self._db = database

    async def make_payment_bank(self, payment: BankPayment) -> None:
        print("realiza pagamento boleto de banco")
        bank = BankPayment()
        bank.billet = payment.billet
        bank.amount = payment.amount
        self._db.add(bank)
        self._db.commit()
        self._db.refresh(bank)
        self.notify()
        return bank

    async def make_payment_consumer(self, payment: ConsumerPayment) -> None:
        print("realiza pagamento boleto de consumo")
        consumer = ConsumerPayment()
        consumer.amount = payment.amount
        consumer.billet = payment.billet
        self._db.add(consumer)
        self._db.commit()
        self._db.refresh(consumer)
        self.notify()
        return consumer
