class Bank_account(object):
    def __init__(self, IBAN, account_no, availabe_funds, transactions):
        self.IBAN = IBAN
        self.account_no = account_no
        self.available_funds = availabe_funds
        self.transactions = transactions

    def deposit(self, money_deposit):
        money_deposit += self.available_funds
        print(money_deposit)

    def withdrawal(self, money_withdrawal):
        money_withdrawal -= self.available_funds
        print(money_withdrawal)
