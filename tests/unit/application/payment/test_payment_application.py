import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from application.payment.payment_application import PaymentApplication
from domain.schemas.bank_payment import BankPayment
from domain.schemas.consumer_payment import ConsumerPayment
from domain.entities.billet_payment import BilletPayment

class TestPaymentApplication(TestCase):

    def setUp(self) -> None:
        self._db = MagicMock()
        self._db.add = MagicMock()
        self._db.commit = MagicMock()
        self.payment = PaymentApplication(self._db)
        self.payment.notify_payment = MagicMock()
        self.bank = BankPayment
        self.bank.amount = "10"
        self.bank.billet = "test1234"
        self.consumer = ConsumerPayment
        self.consumer.billet = "testconsumer"
        self.consumer.amount = "20"

    def test_make_payment_bank(self):
        self.assertEqual(type(self.payment.make_payment_bank(self.bank)), BilletPayment)
        assert self.payment.notify_payment.called is True

    def test_make_consumer_payment(self):
        self.assertEqual(type(self.payment.make_payment_consumer(self.consumer)), BilletPayment)
        assert self.payment.notify_payment.called is True
