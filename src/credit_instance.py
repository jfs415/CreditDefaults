class CreditInstance:
    month = None
    pay = None
    bill_amount = None
    pay_amount = None
    will_default = None

    def __init__(self, month: int, pay: str, bill_amount: int, pay_amount: int, will_default: str):
        self.month = month
        self.pay = pay
        self.bill_amount = bill_amount
        self.pay_amount = pay_amount
        self.will_default = will_default

    def get_month(self):
        return self.month

    def get_pay(self):
        return self.pay

    def get_bill_amount(self):
        return self.bill_amount

    def get_pay_amount(self):
        return self.pay_amount

    def will_default(self):
        return self.will_default

    def __str__(self):
        return "pay: " + self.pay + "; bill: " + str(self.bill_amount) + "; pay_amount: " + str(self.pay_amount) \
                + "; will_default: " + self.will_default
