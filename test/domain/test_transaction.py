from app.domain.transaction import Transaction


class TestTransaction:
    def test_should_be_comparable(self):
        assert Transaction("01/01/2000", 100) != Transaction("01/02/2000", 100)
        assert Transaction("01/02/2000", 200) != Transaction("01/02/2000", 100)
        assert Transaction("01/02/2000", 100) == Transaction("01/02/2000", 100)
