jobs:
	celery -A main.celery worker --loglevel=info -Q consumer_payments,bank_payments