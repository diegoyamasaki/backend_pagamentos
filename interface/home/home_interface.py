import json
from fastapi import APIRouter, Depends
from application.health_check.health_check import HealthCheckApplication
from domain.schemas.health_check import HealthCheck
from infra.database.conection import get_db
from infra.services.payment_service.payment import Payment
from sqlalchemy.orm import Session

home_router = APIRouter()


@home_router.get("/", response_model=HealthCheck)
async def health_check(db: Session = Depends(get_db), payment_service: Payment = Depends(Payment)) -> json:
    return await HealthCheckApplication().validate_backend(db, payment_service)
