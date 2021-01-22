from PaymentProcess import PaymentProcess
from PaymentGateway import PaymentGateway


class PaymentProcessBuilder:
    def __init__(self):
        self.firstProcess = None
        self.lastProcess = None

    def useGateway(self, gateway: PaymentGateway):
        if self.firstProcess is None:
            self.firstProcess = PaymentProcess.PaymentProcess(gateway)
            self.lastProcess = self.firstProcess
        else:
            nextLastProcess = PaymentProcess.PaymentProcess(gateway)
            self.lastProcess.setFallbackProcess(nextLastProcess)
            self.lastProcess = nextLastProcess
        return self

    def build(self):
        return self.firstProcess
