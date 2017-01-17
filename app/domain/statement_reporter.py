from abc import ABC, abstractmethod


class StatementReporter(ABC):
    @abstractmethod
    def report(self, transactions):
        raise NotImplementedError()
