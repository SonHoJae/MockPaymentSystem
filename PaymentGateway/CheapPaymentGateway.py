from abc import ABC, abstractmethod
from random import randint
from PaymentGateway.PaymentGateway import PaymentGateway



class CheapPaymentGateway(PaymentGateway):

    def tryToPay(self, paymentRequest):
        print('Try to pay method on CheapPaymentGateway')
        if randint(0, 10) > 5:
            return 1
        else:
            return 0