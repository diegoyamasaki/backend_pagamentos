import requests
from shared.config import Config


class Payment:

    async def check_service(self):
        response = requests.get(Config.URL_PAYMENT_SERVICE)
        return response.elapsed.total_seconds()
