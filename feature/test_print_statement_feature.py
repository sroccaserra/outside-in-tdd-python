from unittest.mock import Mock, call

from app.domain.bank_account import BankAccount
from app.infrastructure.clock import Clock
from app.infrastructure.console import Console
from app.infrastructure.statement_console_reporter import StatementConsoleReporter
from app.infrastructure.transaction_in_memory_register import TransactionInMemoryRegister


class TestPrintStatementFeature:
    def setup_method(self):
        clock = Mock(Clock)
        clock.today_as_string.side_effect = ['01/04/2014', '02/04/2014', '10/04/2014']
        transaction_register = TransactionInMemoryRegister(clock)

        self.console = Mock(Console)
        statement_reporter = StatementConsoleReporter(self.console)

        self.account = BankAccount(transaction_register, statement_reporter)

    def should_print_a_statement_with_all_transaction(self):
        self.account.deposit(1000)
        self.account.withdraw(100)
        self.account.deposit(500)

        self.account.print_statement()

        calls = [
            call('DATE | AMOUNT | BALANCE'),
            call('10/04/2014 | 500.00 | 1400.00'),
            call('02/04/2014 | -100.00 | 900.00'),
            call('01/04/2014 | 1000.00 | 1000.00'),
        ]
        self.console.print_line.assert_has_calls(calls)
