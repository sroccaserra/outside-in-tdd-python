from unittest.mock import Mock

from app.domain.transaction import Transaction
from app.infrastructure.clock import Clock
from app.infrastructure.transaction_in_memory_register\
    import TransactionInMemoryRegister

TODAY_AS_STRING = "01/02/2012"


class TestTransactionInMemoryRegister:
    def setup_method(self):
        self.clock = Mock(Clock)
        self.clock.today_as_string.return_value = TODAY_AS_STRING
        self.transaction_register = TransactionInMemoryRegister(self.clock)

    def test_should_create_and_store_a_deposit_transaction(self):
        self.transaction_register.add_deposit(100)

        transactions = self.transaction_register.all_transactions()

        assert len(transactions) == 1
        assert transactions[0] == Transaction(TODAY_AS_STRING, 100)

    def test_should_create_and_store_a_withdrawal_transaction(self):
        self.transaction_register.add_withdrawal(100)

        transactions = self.transaction_register.all_transactions()

        assert len(transactions) == 1
        assert transactions[0] == Transaction(TODAY_AS_STRING, -100)
