from decimal import Decimal


class Balance:
    def __init__(self):
        self._balance = Decimal('0')

    @property
    def usd(self) -> Decimal:
        return self._balance

    @usd.setter
    def usd(self, value: Decimal) -> None:
        self._balance = value
