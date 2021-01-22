
class PaymentResult:
    def __init__(self, code):
        self.code = code

    def getResponse(self):
        if str(self.code) == '200':
            return "Successfully processed ( 200 )"
        elif str(self.code) == '400':
            return "Process failed ( 400 )"
        elif str(self.code) == '500':
            return 'Internal Error ( 500 )'