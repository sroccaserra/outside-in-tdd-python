from app.domain.statement_reporter import StatementReporter


class StatementConsoleReporter(StatementReporter):
    def __init__(self, console):
        self.console = console

    def report(self, transactions):
        self.console.print_line('DATE | AMOUNT | BALANCE')
