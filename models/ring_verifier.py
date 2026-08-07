from models.zn import Zn
from models.property_result import PropertyResult
from itertools import product


class RingVerifier:


    zn: Zn
    n: int
    additive_identity: int | None


    def __init__(self, zn: Zn) -> None:
        self.zn = zn
        self.n = self.zn.get_n()
        self.additive_identity = None


    def verify_additive_closure(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result: PropertyResult = self._verify_additive_closure(a, b)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Clausura bajo la suma",
            is_valid = True,
            explanation = "Se verifico que para todos los pares (a, b) pertenecientes a Zn,"
                    " a + b (mod n) tambien pertenece a Zn"
        )


    def verify_multiplicative_closure(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result: PropertyResult = self._verify_multiplicative_closure(a, b)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Clausura bajo el producto",
            is_valid = True,
            explanation = "Se verifico que para todos los pares (a, b) pertenecientes a Zn,"
                        " a * b (mod n) tambien pertenece a Zn"
        )


    def verify_additive_associativity(self) -> PropertyResult:
        for a, b, c in product(range(self.n), range(self.n), range(self.n)):
            result: PropertyResult = self._verify_additive_associativity(a, b, c)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Asociatividad bajo la suma",
            is_valid = True,
            explanation = f"Se verifico que para todas las ternas (a, b, c) pertenecientes a Zn,"
                    " (a + b) + c es igual a a + (b + c)"
        )


    def verify_additive_identity(self) -> PropertyResult:
        is_identity: bool = True

        for e, a in product(range(self.n), range(self.n)):
            if self.zn.add(e, a) != a:
                break
            else:
                self.additive_identity = e

        if is_identity:
            return PropertyResult(
                name = "Elemento neutro en la suma",
                is_valid = True,
                explanation = f"Se encontro el elemento e = {self.additive_identity} perteneciente a Zn"
                        " tal que para todo a perteneciente a Zn, a + e = a"
            )

        return PropertyResult(
            name = "Elemento neutro en la suma",
            is_valid = False,
            explanation = f"No se encontro ningun elemento e pertenciente a Zn"
                    " tal que para todo a perteneciente a Zn, a + e = a"
        )


    def verify_additive_inverses(self) -> PropertyResult:
        identity_result: PropertyResult
        identity: int

        if self.additive_identity is None:
            identity_result = self.verify_additive_identity()

            if not identity_result.is_valid:
                return PropertyResult(
                    name = "Inversos aditivos",
                    is_valid = False,
                    explanation = "No se pueden verificar los inversos aditivos porque no existe un elemento"
                            "neutro aditivo"
                )

        identity = self.additive_identity

        for a, b in product(range(self.n), range(self.n)):
            pass



    def _verify_additive_closure(self, a: int, b: int) -> PropertyResult:
        result: int = self.zn.add(a, b)

        if result not in self.zn.elements():
            return PropertyResult(
                name = "Clausura bajo la suma",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b} se obtuvo que a + b = {result}"
                        " NO pertenece a Zn"
            )

        return PropertyResult(
            name = "Clausura bajo la suma",
            is_valid = True,
            explanation = "Se verifico que para todos los pares (a, b) pertenecientes a Zn,"
                        " a + b (mod n) tambien pertenece a Zn"
        )


    def _verify_multiplicative_closure(self, a: int, b: int) -> PropertyResult:
        result: int = self.zn.multiply(a, b)

        if result not in self.zn.elements():
            return PropertyResult(
                name = "Clausura bajo el producto",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b} se obtuvo que a * b = {result}"
                        " NO pertenece a Zn"
            )

        return PropertyResult(
            name = "Clausura bajo el producto",
            is_valid = True,
            explanation = "Se verifico que para todos los pares (a, b) pertenecientes a Zn,"
                    " a * b (mod n) tambien pertenece a Zn"
        )


    def _verify_additive_associativity(self, a: int, b: int, c: int) -> PropertyResult:
        left: int = self.zn.add(self.zn.add(a, b), c)
        right: int = self.zn.add(a, self.zn.add(b, c))

        if not right == left:
            return PropertyResult(
                name = "Asociatividad bajo la suma",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b}, c = {c}"
                        " (a + b) + c NO es igual a a + (b + c)"
            )

        return PropertyResult(
            name = "Asociatividad bajo la suma",
            is_valid = True,
            explanation = f"Se verifico que para todas las ternas (a, b, c) pertenecientes a Zn,"
                    " (a + b) + c es igual a a + (b + c)"
        )