class BankAccount:
    def __init__(self, transaction_register, statement_reporter):
        self.transaction_register = transaction_register
        self.statement_reporter = statement_reporter

    def deposit(self, amount):
        self.transaction_register.add_deposit(amount)

    def withdraw(self, amount):
        self.transaction_register.add_withdrawal(amount)

    def print_statement(self):
        transactions = self.transaction_register.all_transactions()
        self.statement_reporter.report(transactions)
