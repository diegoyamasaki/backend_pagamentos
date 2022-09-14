from pydantic import BaseModel


class HealthCheck(BaseModel):
    database: str = None
    service: str = None
