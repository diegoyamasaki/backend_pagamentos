jobs:
	celery -A main.celery worker --loglevel=info -Q billet_payments
flower:
	celery -A main.celery flower --post=5555
