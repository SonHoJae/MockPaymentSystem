
class PaymentRequest:
    def __init__(self, price, creditInfo):
        self.price = price
        self.creditInfo = creditInfo

    def getPrice(self):
        return self.price