# Строка графика платежей


class Payment_schedule_row:
    id_contract = 0
    payment = 0
    date = 0
    amount_of_payment = 0
    paid_amount = 0

    def __init__(self, id_contract, payment, date, amount_of_payment, paid_amount):
        self.id_contract = id_contract
        self.payment = payment
        self.date = date
        self.amount_of_payment = amount_of_payment
        self.paid_amount = paid_amount

    def get_payment_schedule_row(self):
        print("Contract number: " + str(self.id_contract) +
              " Payment number " + str(self.payment) +
              " Date: " + str(self.date) +
              " Amount: " + str(self.amount_of_payment) +
              " Paid amount: " + str(self.paid_amount))
