import requests
import json
from retry import retry
from shared.config import Config


class Payment:

    async def check_service(self):
        response = requests.get(Config.URL_PAYMENT_SERVICE)
        return response.elapsed.total_seconds()

    
    @retry(exceptions=requests.exceptions.ConnectionError, delay=1, backoff=2, tries=5)
    async def notify_payment(self, data: dict):
        response = requests.post(Config.URL_PAYMENT_SERVICE, json=json.dumps(data))
        return response.json()
