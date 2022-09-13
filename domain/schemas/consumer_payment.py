from typing import Optional

from pydantic import BaseModel

#https://fastapi.tiangolo.com/tutorial/sql-databases/
class ConsumerPayment(BaseModel):
    id: Optional[int]
    billet: str
    amount: str

    class Config:
        orm_mode = True