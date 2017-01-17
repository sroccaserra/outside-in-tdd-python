from unittest.mock import Mock

from app.infrastructure.console import Console
from app.infrastructure.statement_console_reporter import StatementConsoleReporter

NO_TRANSACTIONS = []


class TestStatementConsoleReporter:
    def test_should_always_print_the_header(self):
        console = Mock(Console)
        statement_reporter = StatementConsoleReporter(console)

        statement_reporter.report(NO_TRANSACTIONS)

        console.print_line.assert_called_with('DATE | AMOUNT | BALANCE')
