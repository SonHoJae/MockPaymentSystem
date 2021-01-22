from PaymentProcess.PaymentResult import PaymentResult


class PaymentProcess:

    def __init__(self, gateway):
        self.paymentRequest = None
        self.fallbackProcess = None
        self.gateway = gateway

    def process(self, paymentRequest):
        response = self.gateway.tryToPay(paymentRequest)
        if response == 1:  # success
            return PaymentResult(200).getResponse()
        else:
            if self.fallbackProcess != None:
                return self.fallbackProcess.process(paymentRequest)
            if response == 0:
                return PaymentResult(400).getResponse()

    def setFallbackProcess(self, fallbackProcess):
        self.fallbackProcess = fallbackProcess


class FailedPaymentProcess(PaymentProcess):

    def process(self, paymentRequest):
        return PaymentResult(400).getResponse()
