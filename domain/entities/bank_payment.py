from domain.entities.billet_payment import BilletPayment
from infra.database.conection import Base

class BankPayment(BilletPayment, Base):
    __tablename__ = "bank_payment"
