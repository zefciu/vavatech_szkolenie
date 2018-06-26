class Validated:
    """Przechowuje liczbę, którą waliduje przy zapisie"""

    def __init__(self, x, lower, higher):
        self._x = x
        self.lower = lower
        self.higher = higher

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < self.lower or value > self.higher:
            raise ValueError('Out of bounds')
        self._x = value
