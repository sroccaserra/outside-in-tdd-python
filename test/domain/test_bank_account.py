from unittest.mock import Mock

from domain import BankAccount
from domain import StatementReporter
from domain import Transaction
from domain import TransactionRegister


class TestBankAccount:
    def setup_method(self):
        self.transaction_register = Mock(TransactionRegister)
        self.statement_reporter = Mock(StatementReporter)
        self.account = BankAccount(self.transaction_register,
                                   self.statement_reporter)

    def should_store_a_deposit(self):
        self.account.deposit(1000)
        self.transaction_register.add_deposit.assert_called_with(1000)

    def should_store_a_withdrawal(self):
        self.account.withdraw(1000)
        self.transaction_register.add_withdrawal.assert_called_with(1000)

    def should_print_a_statement_with_all_transactions(self):
        transactions = [Transaction('17/02/1976', 100)]
        self.transaction_register.all_transactions.return_value = transactions

        self.account.print_statement()

        self.statement_reporter.report.assert_called_with(transactions)
