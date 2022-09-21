from sqlalchemy.orm import Session
from typing import List
from domain.entities.billet_payment import BilletPayment
from domain.enum.billet_type import BilletType
from shared.notify import Notify
from shared.observer import Observer
from application.cashback import CachBackApplication
from infra.services.payment_service.payment import Payment
from domain.job.tasks import queue_notify_payment


class PaymentApplication(Notify):

    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        
    def notify(self, payment: any) -> None:
        for observer in self._observers:
            observer.update(self, payment)

    def __init__(self, database: Session):
        self._db = database
        self.attach(CachBackApplication())

    @property
    def payment_service(self):
        return Payment()

    def make_payment_bank(self, payment: BilletPayment) -> None:
        print("realiza pagamento boleto de banco")
        bank = BilletPayment()
        bank.billet = payment.billet
        bank.amount = payment.amount
        bank.billet_type = BilletType.bank
        self._db.add(bank)
        self._db.commit()
        self.notify_payment(bank.to_json())
        self._db.refresh(bank)
        return bank

    def make_payment_consumer(self, payment: BilletPayment) -> None:
        print("realiza pagamento boleto de consumo")
        consumer = BilletPayment()
        consumer.amount = payment.amount
        consumer.billet = payment.billet
        consumer.billet_type = BilletType.consumer
        self._db.add(consumer)
        self._db.commit()
        self.notify_payment(consumer.to_json())
        self._db.refresh(consumer)
        return consumer

    def notify_payment(self, payment: any):
        try:
            data = self.payment_service.notify_payment(payment)
            if data:
                data_payment = self._db.query(BilletPayment).filter(BilletPayment.id == payment['id']).first()
                data_payment.transaction_id = data['transactiondId']
                self._db.commit()
                self.notify(data_payment.to_json())
        except Exception as e:
            print('erro! colocando na fila')
            queue_notify_payment(payment)









