from fastapi import Depends
from celery import shared_task
from celery.utils.log import get_task_logger
from infra.database.connection import Session_Local

log = get_task_logger(__name__)


def queue_notify_payment(payment):
    process_payments.apply_async([payment])


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='billet_payments:process_payments')
def process_payments(self, payment):
    try:
        from application.payment.payment_application import PaymentApplication
        log.info('process_bank_payments')
        log.info(payment)
        db = Session_Local()
        app = PaymentApplication(db)
        app.notify_payment(payment)
    finally:
        db.close()
    return payment




