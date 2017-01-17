from datetime import date

from app.infrastructure.clock import Clock


class TestableClock(Clock):
    @staticmethod
    def today():
        return date(1976, 2, 17)


class TestClock:
    def test_should_return_today_as_string(self):
        clock = TestableClock()
        assert clock.today_as_string() == "17/02/1976"
