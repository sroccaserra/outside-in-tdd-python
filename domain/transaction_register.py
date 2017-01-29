from abc import ABC, abstractmethod


class TransactionRegister(ABC):
    @abstractmethod
    def add_deposit(self, amount):
        pass

    @abstractmethod
    def add_withdrawal(self, amount):
        pass

    @abstractmethod
    def all_transactions(self):
        pass
