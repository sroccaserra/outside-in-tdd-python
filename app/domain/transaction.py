class Transaction:
    def __init__(self, date_as_string, amount):
        self.date_as_string = date_as_string
        self.amount = amount

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if type(other) is type(self):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
