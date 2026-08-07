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


    def addition_table(self) -> list[list[int]]:
        table: list[list[int]] = []

        for i in range(self.n):
            sublist: list[int] = []
            for j in range(self.n):
                sublist.append(self.add(i, j))
            table.append(sublist)

        return table


    def multiplication_table(self) -> list[list[int]]:
        table: list[list[int]] = []

        for i in range(self.n):
            sublist: list[int] = []
            for j in range(self.n):
                sublist.append(self.multiply(i, j))
            table.append(sublist)

        return table


    def get_n(self) -> int:
        return self.n