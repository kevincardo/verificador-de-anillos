class Zn:


    n: int


    def __init__(self, n: int) -> None:
        self.n = n


    def elements(self) -> list[int]:
        return list(range(self.n))


    def add(self, a: int, b: int) -> int:
        return (a + b) % self.n


    def multiply(self, a: int, b: int) -> int:
        return (a * b) % self.n