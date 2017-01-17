from unittest.mock import Mock, call

from app.domain.transaction import Transaction
from app.infrastructure.console import Console
from app.infrastructure.statement_console_reporter import StatementConsoleReporter

NO_TRANSACTIONS = []


class TestStatementConsoleReporter:
    def setup_method(self):
        self.console = Mock(Console)
        self.statement_reporter = StatementConsoleReporter(self.console)

    def test_should_always_print_the_header(self):
        self.statement_reporter.report(NO_TRANSACTIONS)

        self.console.print_line.assert_called_with('DATE | AMOUNT | BALANCE')

    def test_should_print_all_transactions(self):
        transactions = [
            Transaction('01/04/2014', 1000),
            Transaction('02/04/2014', -100),
            Transaction('10/04/2014', 500),
        ]
        self.statement_reporter.report(transactions)

        calls = [
            call('DATE | AMOUNT | BALANCE'),
            call('10/04/2014 | 500.00 | 1400.00'),
            call('02/04/2014 | -100.00 | 900.00'),
            call('01/04/2014 | 1000.00 | 1000.00'),
        ]
        self.console.print_line.assert_has_calls(calls)
