from sqlalchemy import Column, String, Integer
from infra.database.conection import Base


class BankPayment(Base):
    __tablename__ = "bank_payment"
    id = Column(Integer, primary_key=True, index=True)
    billet = Column(String)
    amount = Column(String)



