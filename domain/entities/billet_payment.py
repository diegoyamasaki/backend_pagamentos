from sqlalchemy import Column, String, Integer, Enum
from infra.database.conection import Base
from domain.enum.billet_type import BilletType


class BilletPayment(Base):
    __tablename__ = "billet_payment"
    id = Column(Integer, primary_key=True, index=True)
    billet = Column(String)
    amount = Column(String)
    billet_type = Column(Enum(BilletType))
    transaction_id = Column(String)

    def to_json(self):
        return {
            "id": self.id,
            "billet": self.billet,
            "amount": self.amount,
            "transaction_id": self.transaction_id
        }



