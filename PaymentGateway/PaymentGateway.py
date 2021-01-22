from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def tryToPay(self, paymentRequest):
        raise NotImplementedError()