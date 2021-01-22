import datetime


class CreditCard:
    def __init__(self):
        self.creditCardNumber = None
        self.cardHolder = None
        self.expirationDate = None
        self.securityCode = None
        self.amount = None

    def setCreditCardNumber(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber

    def setCardHolder(self, cardHolder):
        self.cardHolder = cardHolder

    def setExpirationDate(self, expirationDate):
        self.expirationDate = expirationDate

    def setSecurityCode(self, securityCode):
        try:
            self.securityCode = int(securityCode)
        except:
            raise ValueError()

    def setAmount(self, amount):
        self.amount = amount

    def verify(self):
        self.verifySecurityCode()
        self.verifyCardNumber()
        self.verifyExpiraztionDate()
        self.verifyAmount()
        self.verifyCardHolder()

    def verifySecurityCode(self):
        if not (100 <= self.securityCode <= 999):
            print("The securityCode is incorrect")
            raise ValueError()

    def verifyCardHolder(self):
        if self.cardHolder == None or not isinstance(self.cardHolder, str):
            print("The cardHolder is incorrect")
            raise ValueError()

    def verifyCardNumber(self):
        if self.creditCardNumber == None or not isinstance(self.creditCardNumber, str):
            # TODO
            # Add valid card number policy
            print("The creditCardNumber is incorrect")
            raise ValueError()

    def verifyExpiraztionDate(self):
        if self.expirationDate == None or not isinstance(self.expirationDate, datetime.datetime):
            print("expirationDate format is incorrect")
            raise ValueError()
        if self.expirationDate < datetime.datetime.now():
            print("The card is expired")
            raise Exception()

    def verifyAmount(self):
        if int(self.amount) < 0:
            print("Invalid balance")
            raise Exception()
