from domain import Transaction
from domain import TransactionRegister


class TransactionInMemoryRegister(TransactionRegister):
    def __init__(self, clock):
        self.clock = clock
        self.transactions = []

    def add_deposit(self, amount):
        today_as_string = self.clock.today_as_string()
        self.transactions.append(Transaction(today_as_string, amount))

    def add_withdrawal(self, amount):
        today_as_string = self.clock.today_as_string()
        self.transactions.append(Transaction(today_as_string, -amount))

    def all_transactions(self):
        return self.transactions
