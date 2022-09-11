from typing import Optional
from abc import ABC
from sqlalchemy import Column, String, Integer

class BilletPayment(ABC):
    id = Column(Integer, primary_key=True, index=True)
    billet = Column(String)
    amount =Column(String)
