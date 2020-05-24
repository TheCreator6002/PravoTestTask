from Domain.Contract import Contract


class Mapper:
    id_contract = 0
    period_months = 0
    amount_money = 0
    start_contract_date = 0

    def __init__(self, id_contract, period_months, amount_money, start_contract_date):
        self.id_contract = id_contract
        self.period_months = period_months
        self.amount_money = amount_money
        self.start_contract_date = start_contract_date

    def create(self):
        return Contract(self.id_contract,
                        self.period_months,
                        self.amount_money,
                        self.start_contract_date)
