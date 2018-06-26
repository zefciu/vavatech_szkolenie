class PrimesIterator:
    """Iteruje po liczbach pierwszych"""

    def __init__(self):
        self.primes = []
        self.current = 2

    def __iter__(self):
        return type(self)()

    def __next__(self):
        while True:
            for prime in self.primes:
                if not self.current % prime:
                    self.current += 1
                    break
            else:
                self.primes.append(self.current)
                self.current += 1
                return self.current - 1
