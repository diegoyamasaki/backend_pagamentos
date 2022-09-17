from typing import Optional
from pydantic import BaseModel


class ConsumerPayment(BaseModel):
    id: Optional[int]
    billet: str
    amount: str

    class Config:
        orm_mode = True