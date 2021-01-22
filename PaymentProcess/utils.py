
from PaymentGateway.CheapPaymentGateway import CheapPaymentGateway
from PaymentGateway.ExpensivePaymentGateway import ExpensivePaymentGateway
from PaymentGateway.PremiumPaymentGateway import PremiumPaymentGateway
from PaymentProcess.PaymentProcess import FailedPaymentProcess

def chooseProcess(paymentProcessBuilder, request):
    price = request.getPrice()

    if int(price) > int(request.creditInfo):
        return FailedPaymentProcess()

    if 0 < price < 20:
        return paymentProcessBuilder.useGateway(CheapPaymentGateway()).build()
    elif 20 <= price < 500:
        return paymentProcessBuilder.useGateway(ExpensivePaymentGateway()) \
            .useGateway(CheapPaymentGateway()).build()
    elif price >= 500:
        return paymentProcessBuilder.useGateway(PremiumPaymentGateway()) \
            .useGateway(PremiumPaymentGateway()) \
            .useGateway(PremiumPaymentGateway()).build()

