from domain import BankAccount
from infrastructure import Clock
from infrastructure import Console
from infrastructure import StatementConsoleReporter
from infrastructure import TransactionInMemoryRegister


def main():
    clock = Clock()
    transaction_register = TransactionInMemoryRegister(clock)
    console = Console()
    statement_reporter = StatementConsoleReporter(console)
    bank_account = BankAccount(transaction_register, statement_reporter)

    bank_account.deposit(1000)
    bank_account.withdraw(400)
    bank_account.deposit(100)

    bank_account.print_statement()


if __name__ == '__main__':
    main()
