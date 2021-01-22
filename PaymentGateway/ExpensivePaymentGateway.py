from abc import ABC, abstractmethod
from random import randint

from PaymentGateway.PaymentGateway import PaymentGateway


class ExpensivePaymentGateway(PaymentGateway):

    def tryToPay(self, paymentRequest):
        print('Try to pay method on ExpensivePaymentGateway')
        if randint(0, 10) > 5:
            return 1
        else:
            return 0