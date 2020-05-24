# Класс с полями важными для предметной области (пока что все столбцы из таблицы)
from datetime import datetime
from .Payment_schedule import Payment_schedule


class Contract:
    id_contract = 0
    period_months = 0
    amount_money = 0
    start_contract_date = 0
    term = 0

    def __init__(self, id_contract, period_months, amount_money, start_contract_date):
        format_time = '%Y-%m-%d'
        self.id_contract = id_contract
        self.period_months = period_months
        self.amount_money = amount_money
        self.start_contract_date = datetime.strptime(start_contract_date, format_time)

    def payment_calculation(self, term):
        self.term = term
        number_of_payments = (self.term * 12) / self.period_months  # Количество платежей
        amount_of_payment = self.amount_money / number_of_payments  # Сумма платежа
        payment_schedule = Payment_schedule(self.id_contract,
                                            number_of_payments,
                                            amount_of_payment,
                                            self.period_months,
                                            self.start_contract_date)
        payment_schedule.add_payment_schedule()

