from domain.schemas.health_check import HealthCheck
from httpx import RequestError
from sqlalchemy.exc import SQLAlchemyError


class HealthCheckApplication:

    _health: HealthCheck

    def __init__(self):
        self._health = HealthCheck()

    async def validate_backend(self, db, payment_service):
        try:
            db.execute('SELECT 1')
            self._health.database = 'ok'
            self._health.service = await payment_service.check_service()
        except RequestError:
            self._health.service = "error"
        except SQLAlchemyError:
            self._health.database = 'error'
        return self._health


