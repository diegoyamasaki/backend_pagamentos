import requests
import json
from shared.config import Config



class Payment:

    async def check_service(self):
        response = requests.get(Config.URL_PAYMENT_SERVICE)
        return response.elapsed.total_seconds()

    def notify_payment(self, data: dict):
        response = requests.post(Config.URL_PAYMENT_SERVICE, json=json.dumps(data))
        return json.loads(response.text.replace("\n", '').replace(',', '').strip())

