
from PaymentProcess.PaymentProcessBuilder import PaymentProcessBuilder
from PaymentProcess.PaymentRequeest import PaymentRequest
from PaymentProcess.PaymentResult import PaymentResult
from PaymentProcess.utils import chooseProcess

if __name__ == "__main__":
    try:
        paymentProcessBuilder = PaymentProcessBuilder()
        request = PaymentRequest(400)
        paymentProcess = chooseProcess(paymentProcessBuilder, request)
        result = paymentProcess.process(request)
        print(result)
    except:
        result = PaymentResult(500).getResponse()
        print(result)
