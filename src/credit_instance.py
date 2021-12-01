class CreditInstance:
    month = None
    pay_type = None
    bill_amount = None
    pay_amount = None
    will_default = None
    data = None


    def __init__(self, month: int, pay_type: str, bill_amount: int, pay_amount: int, will_default: str):
        self.month = month
        self.pay_type = pay_type
        self.bill_amount = bill_amount
        self.pay_amount = pay_amount
        self.will_default = will_default
        self.data = {
            "pay_type": pay_type,
            "bill_amount": bill_amount,
            "pay_amount": pay_amount
        }


    def get_month(self):
        return self.month


    def get_pay(self):
        return self.pay_type


    def get_bill_amount(self):
        return self.bill_amount


    def get_pay_amount(self):
        return self.pay_amount


    def will_default(self):
        return self.will_default


    def get_data(self):
        return self.data
