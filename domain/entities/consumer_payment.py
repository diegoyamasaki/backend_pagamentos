from sqlalchemy import Column, String, Integer
from infra.database.conection import Base


class ConsumerPayment(Base):
    __tablename__ = "consumer_payment"
    id = Column(Integer, primary_key=True, index=True)
    billet = Column(String)
    amount = Column(String)
