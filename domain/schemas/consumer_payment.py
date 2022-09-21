from typing import Optional
from pydantic import BaseModel


class ConsumerPayment(BaseModel):
    id: Optional[int]
    billet: str
    amount: str

    def to_json(self):
        return {
            "billet": self.billet,
            "amount": self.amount
        }

    class Config:
        orm_mode = True
