from datetime import date


class Clock:
    def today_as_string(self):
        today = self.today()
        return today.strftime('%d/%m/%Y')

    @staticmethod
    def today():
        return date.today()
