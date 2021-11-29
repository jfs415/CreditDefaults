class CreditInstance:
    month = None
    pay = None
    bill_amount = None
    pay_amount = None

    def __init__(self, month: int, pay: str, bill_amount: int, pay_amount: int):
        self.month = month
        self.pay = pay
        self.bill_amount = bill_amount
        self.pay_amount = pay_amount

    def get_month(self):
        return self.month

    def get_pay(self):
        return self.pay

    def get_bill_amount(self):
        return self.bill_amount

    def get_pay_amount(self):
        return self.pay_amount
