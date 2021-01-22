from flask import Flask

from CreditCard.CreditCard import CreditCard
from PaymentProcess.PaymentProcessBuilder import PaymentProcessBuilder
from PaymentProcess.PaymentRequeest import PaymentRequest
from PaymentProcess.PaymentResult import PaymentResult
from PaymentProcess.utils import chooseProcess
import datetime


app = Flask(__name__)

@app.route('/ProcessPayment')
def mockProcessPayment():
    try:
        paymentProcessBuilder = PaymentProcessBuilder()
        # CreditCard information will be fetched from web
        creditInfo = CreditCard()
        creditInfo.setCreditCardNumber("123456789")
        creditInfo.setAmount("0")
        creditInfo.setExpirationDate(datetime.datetime.now() + datetime.timedelta(days=1))
        creditInfo.setSecurityCode("123")
        creditInfo.setCardHolder("Hojae")
        creditInfo.verify()
        request = PaymentRequest(400, creditInfo)
        paymentProcess = chooseProcess(paymentProcessBuilder, request)
        result = paymentProcess.process(request)
        return result
    except:
        result = PaymentResult(500).getResponse()
        return result


if __name__ == '__main__':
    app.run()