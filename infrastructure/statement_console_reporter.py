from domain import StatementReporter


class StatementConsoleReporter(StatementReporter):
    def __init__(self, console):
        self.console = console

    def report(self, transactions):
        self.console.print_line('DATE | AMOUNT | BALANCE')

        balance = 0
        report_lines = []
        for transaction in transactions:
            balance += transaction.amount
            report_lines.append(self.report_line(transaction, balance))

        for report_line in reversed(report_lines):
            self.console.print_line(report_line)

    @staticmethod
    def report_line(transaction, balance):
        return '{0} | {1:.2f} | {2:.2f}'.format(transaction.date_as_string,
                                                transaction.amount,
                                                balance)
