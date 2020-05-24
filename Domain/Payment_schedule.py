# График платежей
from dateutil.relativedelta import *
from .Payment_schedule_row import Payment_schedule_row


class Payment_schedule:
    id_contract = 0
    number_of_payments = 0
    amount_of_payment = 0
    period_months = 0
    start_contract_date = 0

    def __init__(self,
                 id_contract,
                 number_of_payments,
                 amount_of_payment,
                 period_months,
                 start_contract_date):
        self.id_contract = id_contract
        self.number_of_payments = number_of_payments
        self.amount_of_payment = amount_of_payment
        self.period_months = period_months
        self.start_contract_date = start_contract_date

    def add_payment_schedule(self):
        start_payment = 1
        paid_amount = self.amount_of_payment
        payment = start_payment
        date = self.start_contract_date
        while payment <= self.number_of_payments:
            Payment_schedule_row(self.id_contract,
                                 payment,
                                 date,
                                 self.amount_of_payment,
                                 paid_amount).get_payment_schedule_row()
            date += relativedelta(months=+self.period_months)
            payment += 1
            paid_amount += self.amount_of_payment


