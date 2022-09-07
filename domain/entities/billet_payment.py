from pydantic import BaseModel


class BilletPayment(BaseModel):
    billet: str = "826500000011323116990009002022153320476101001040"
    amount: str = "70.24"
