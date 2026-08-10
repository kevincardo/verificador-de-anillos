from models.zn import Zn
from models.property_result import PropertyResult
from itertools import product
from models.verification_result import VerificationResult


class RingVerifier:


    zn: Zn
    n: int
    additive_identity: int | None
    multiplicative_identity: int | None
    additive_inverses: dict[int, int]
    multiplicative_inverses: dict[int, int]


    def __init__(self, zn: Zn) -> None:
        self.zn = zn
        self.n = self.zn.get_n()
        self.additive_identity = None
        self.multiplicative_identity = None
        self.additive_inverses = {}
        self.multiplicative_inverses = {}


    def verify_additive_closure(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result: PropertyResult = self._verify_additive_closure(a, b)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Clausura bajo la suma",
            is_valid = True,
            explanation = f"Se verifico que para todos los pares (a, b) pertenecientes a Z{self.n},"
                    f" a + b (mod n) tambien pertenece a Z{self.n}"
        )


    def verify_multiplicative_closure(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result: PropertyResult = self._verify_multiplicative_closure(a, b)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Clausura bajo el producto",
            is_valid = True,
            explanation = f"Se verifico que para todos los pares (a, b) pertenecientes a Z{self.n},"
                        f" a * b (mod n) tambien pertenece a Z{self.n}"
        )


    def verify_additive_associativity(self) -> PropertyResult:
        for a, b, c in product(range(self.n), range(self.n), range(self.n)):
            result: PropertyResult = self._verify_additive_associativity(a, b, c)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Asociatividad bajo la suma",
            is_valid = True,
            explanation = f"Se verifico que para todas las ternas (a, b, c) pertenecientes a Z{self.n},"
                    " (a + b) + c es igual a a + (b + c)"
        )


    def verify_additive_identity(self) -> PropertyResult:
        for e in self.zn.elements():
            is_identity = True

            for a in self.zn.elements():
                if self.zn.add(e, a) != a or self.zn.add(a, e) != a:
                    is_identity = False
                    break

            if is_identity:
                self.additive_identity = e

                return PropertyResult(
                    name = "Elemento neutro en la suma",
                    is_valid = True,
                    explanation = f"Se encontró el elemento e = {e} perteneciente a Z{self.n} "
                            f"tal que para todo a perteneciente a Z{self.n}, "
                            "e + a = a = a + e = a."
                )

        self.additive_identity = None

        return PropertyResult(
            name = "Elemento neutro en la suma",
            is_valid = False,
            explanation = f"No se encontró ningún elemento e perteneciente a Z{self.n} "
                    f"tal que para todo a perteneciente a Z{self.n}, "
                    "e + a = a y a + e = a."
        )


    def verify_additive_inverses(self) -> PropertyResult:
        if self.additive_identity is None:
            identity_result: PropertyResult = self.verify_additive_identity()

            if not identity_result.is_valid:
                return PropertyResult(
                    name = "Inversos aditivos",
                    is_valid = False,
                    explanation = "No se pueden verificar los inversos aditivos"
                            " porque no existe un elemento neutro aditivo."
                )

        identity = self.additive_identity
        self.additive_inverses.clear()

        for a in self.zn.elements():
            found_inverse = False

            for b in self.zn.elements():

                if self.zn.add(a, b) == identity and self.zn.add(b, a) == identity:
                    self.additive_inverses[a] = b
                    found_inverse = True
                    break

            if not found_inverse:
                return PropertyResult(
                    name = "Inversos aditivos",
                    is_valid = False,
                    explanation = f"El elemento {a} no posee un inverso aditivo "
                )

        return PropertyResult(
            name = "Inversos aditivos",
            is_valid = True,
            explanation = f"Todo elemento de Z{self.n} posee un inverso aditivo "
                f"respecto al elemento neutro {identity}."
        )


    def verify_additive_commutativity(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result1: int = self.zn.add(a, b)
            result2: int = self.zn.add(b, a)

            if result1 != result2:
                return PropertyResult(
                    name = "Conmutatividad para la suma",
                    is_valid = False,
                    explanation = f"Existe la suma {a} + {b} = {result1}"
                            f" que no es igual a {b} + {a} = {result2} "
                )

        return PropertyResult(
            name = "Conmutatividad para la suma",
            is_valid = True,
            explanation = f"Se verifico que para todo numero perteneciente a Z{self.n} a + b = b + a"
        )


    def verify_multiplicative_associativity(self) -> PropertyResult:
        for a, b, c in product(range(self.n), range(self.n), range(self.n)):
            result: PropertyResult = self._verify_multiplicative_associativity(a, b, c)

            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Asociatividad para el producto",
            is_valid = True,
            explanation = f"Para todo a, b, c pertenecientes a Z{self.n}"
            " (a * b) * c es igual a a * (b * c)"
        )


    def verify_left_distributivity(self) -> PropertyResult:
        for a, b, c in product(range(self.n), range(self.n), range(self.n)):
            left: int = self.zn.multiply(a, self.zn.add(b, c))
            right: int = self.zn.add(self.zn.multiply(a, b), self.zn.multiply(a, c))

            if not left == right:
                return PropertyResult(
                    name = "Distributividad por la izquierda",
                    is_valid = False,
                    explanation = f"Existe un a = {a}, b = {b}, c = {c} pertencientes a Z{self.n}"
                            f" tal que a * (b + c) = {left} NO es igual a a * b + a * c = {right}"
                )

        return PropertyResult(
            name = "Distributividad por la izquierda",
            is_valid = True,
            explanation = f"Para todo a, b, c pertenecientes a Z{self.n}"
                    "se cumple que a * (b + c) = a * b + a * c"
            )


    def verify_right_distributivity(self) -> PropertyResult:
        for a, b, c in product(range(self.n), range(self.n), range(self.n)):
            left: int = self.zn.multiply(self.zn.add(a, b), c)
            right: int = self.zn.add(self.zn.multiply(a, c), self.zn.multiply(b, c))

            if not left == right:
                return PropertyResult(
                    name = "Distributividad por la izquierda",
                    is_valid = False,
                    explanation = f"Existe un a = {a}, b = {b}, c = {c} pertencientes a Z{self.n}"
                                f" tal que (a + b) * c = {left} NO es igual a a * c + b * c = {right}"
                )

        return PropertyResult(
            name = "Distributividad por la izquierda",
            is_valid = True,
            explanation = f"Para todo a, b, c pertenecientes a Z{self.n}"
                    " se cumple que (a + b) * c = a * c + b * c"
        )


    def verify_distributivity(self) -> PropertyResult:
        is_distributive_in_left: bool = self.verify_left_distributivity().is_valid
        is_distributive_in_right: bool = self.verify_right_distributivity().is_valid

        if not is_distributive_in_left or not is_distributive_in_right:
            return PropertyResult(
                name = "Distributividad",
                is_valid = False,
                explanation = f"Para todo a, b, c perteneciente a Z{self.n}"
                        f" no se cumple la distributividad en izquierda y derecha"
            )

        return PropertyResult(
            name = "Distributividad",
            is_valid = True,
            explanation = f"Para todo a, b, c perteneciente a Z{self.n}"
                    " se cumple que a * (b + c) = a * b + a * c y"
                    " se cumple que (a + b) * c = a * b + a * c"
        )


    def verify_multiplicative_commutativity(self) -> PropertyResult:
        for a, b in product(range(self.n), range(self.n)):
            result: PropertyResult = self._verify_multiplicative_commutativity(a, b)
            if not result.is_valid:
                return result

        return PropertyResult(
            name = "Conmutatividad para el producto",
            is_valid = True,
            explanation = f"Se verifico que para todo a, b pertenecientes a Z{self.n} "
                    "a * b = b * a"
        )


    def verify_multiplicative_identity(self) -> PropertyResult:
        for e in self.zn.elements():
            is_identity = True
            for a in self.zn.elements():
                if self.zn.multiply(e, a) != a or self.zn.multiply(a, e) != a:
                    is_identity = False
                    break

            if is_identity:
                self.multiplicative_identity = e

                return PropertyResult(
                    name = "Elemento neutro en el producto",
                    is_valid = True,
                    explanation = (
                        f"Se encontró el elemento e = {e} perteneciente a Z{self.n} "
                        "tal que para todo a perteneciente a Zn, "
                        "e * a = a y a * e = a."
                    )
                )

        self.multiplicative_identity = None

        return PropertyResult(
            name = "Elemento neutro en el producto",
            is_valid = False,
            explanation = (
                f"No se encontró ningún elemento e perteneciente a Z{self.n} "
                "tal que para todo a perteneciente a Zn, "
                "e * a = a y a * e = a."
            )
        )


    def verify_multiplicative_inverses(self) -> PropertyResult:
        if self.multiplicative_identity is None:
            identity_result = self.verify_multiplicative_identity()

            if not identity_result.is_valid:
                return PropertyResult(
                    name="Inversos multiplicativos",
                    is_valid=False,
                    explanation=(
                        "No se pueden verificar los inversos multiplicativos "
                        "porque no existe un elemento neutro multiplicativo."
                    )
                )

        identity = self.multiplicative_identity
        self.multiplicative_inverses.clear()

        for a in self.zn.elements():
            if a == 0:
                continue

            found_inverse = False
            for b in self.zn.elements():
                if self.zn.multiply(a, b) == identity and self.zn.multiply(b, a) == identity:
                    self.multiplicative_inverses[a] = b
                    found_inverse = True
                    break

            if not found_inverse:
                return PropertyResult(
                    name = "Inversos multiplicativos",
                    is_valid = False,
                    explanation = f"El elemento {a} no posee un inverso multiplicativo "
                            f"en Z{self.n}."
                )

        return PropertyResult(
            name = "Inversos multiplicativos",
            is_valid = True,
            explanation = f"Todo elemento distinto de 0 de Z{self.n} posee "
                    f"un inverso multiplicativo respecto al elemento "
                    f"neutro {identity}."
        )


    def verify_all(self) -> VerificationResult:
        additive_closure: PropertyResult = self.verify_additive_closure()
        additive_associativity: PropertyResult = self.verify_additive_associativity()
        additive_identity: PropertyResult = self.verify_additive_identity()
        additive_inverses: PropertyResult = self.verify_additive_inverses()
        additive_commutativity: PropertyResult = self.verify_additive_commutativity()

        multiplicative_closure: PropertyResult = self.verify_multiplicative_closure()
        multiplicative_associativity: PropertyResult = self.verify_multiplicative_associativity()
        multiplicative_identity: PropertyResult = self.verify_multiplicative_identity()
        multiplicative_inverses: PropertyResult = self.verify_multiplicative_inverses()
        multiplicative_commutativity: PropertyResult = self.verify_multiplicative_commutativity()

        distributivity: PropertyResult = self.verify_distributivity()

        additive_group: PropertyResult = PropertyResult(
            name = "Grupo bajo la suma",
            is_valid = additive_closure.is_valid
                    and additive_inverses.is_valid
                    and additive_identity.is_valid
                    and additive_associativity.is_valid,
            explanation = "La suma cumple todas las propiedades necesarias para ser un grupo."
        )

        additive_abelian_group: PropertyResult = PropertyResult(
            name = "Grupo Abeliano bajo la suma",
            is_valid = additive_group.is_valid
                    and distributivity.is_valid,
            explanation = "La suma cumple todas las propiedades necesarias para ser un grupo abeliano."
        )

        multiplicative_semigroup: PropertyResult = PropertyResult(
            name = "Semigrupo bajo el producto",
            is_valid = multiplicative_associativity.is_valid
                    and multiplicative_closure.is_valid,
            explanation = "El producto cumple todas las propiedades necesarias para ser un semigrupo."
        )

        ring: PropertyResult = PropertyResult(
            name = "Anillo",
            is_valid = additive_abelian_group.is_valid
                    and multiplicative_semigroup.is_valid
                    and distributivity.is_valid,
            explanation = "Es anillo porque es un grupo abeliano bajo la suma, semigrupo bajo el producto y "
                    "es distributivo tanto por izquierda como por derecha."
        )

        commutative_ring: PropertyResult = PropertyResult(
            name = "Anillo conmutativo",
            is_valid = ring.is_valid
                    and multiplicative_commutativity.is_valid,
            explanation = "Es anillo conmutativo porque aparte de ser anillo su producto es conmutativo."
        )

        field: PropertyResult = PropertyResult(
            name = "Cuerpo",
            is_valid = commutative_ring.is_valid
                    and multiplicative_identity.is_valid
                    and multiplicative_inverses.is_valid,
            explanation = "Es cuerpo (o campo) porque es un anillo conmutativo que tiene un elemento identidad y "
                    "para todos los elementos distintos de 0, existe un inverso multiplicativo"
        )

        return VerificationResult(
            n = self.n,
            additive_group = additive_group,
            multiplicative_semigroup = multiplicative_semigroup,
            additive_abelian_group = additive_abelian_group,
            ring = ring,
            commutative_ring = commutative_ring,
            field = field,
            additive_identity = self.additive_identity,
            additive_inverses = self.additive_inverses,
            multiplicative_inverses = self.multiplicative_inverses,
            multiplicative_identity = self.multiplicative_identity,
            addition_table = self.zn.addition_table(),
            multiplication_table = self.zn.multiplication_table(),
        )


    def _verify_additive_closure(self, a: int, b: int) -> PropertyResult:
        result: int = self.zn.add(a, b)

        if result not in self.zn.elements():
            return PropertyResult(
                name = "Clausura bajo la suma",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b} se obtuvo que a + b = {result}"
                        f" NO pertenece a Z{self.n}"
            )

        return PropertyResult(
            name = "Clausura bajo la suma",
            is_valid = True,
            explanation = f"Se verifico que para todos los pares (a, b) pertenecientes a Z{self.n},"
                        f" a + b (mod n) tambien pertenece a Z{self.n}"
        )


    def _verify_multiplicative_closure(self, a: int, b: int) -> PropertyResult:
        result: int = self.zn.multiply(a, b)

        if result not in self.zn.elements():
            return PropertyResult(
                name = "Clausura bajo el producto",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b} se obtuvo que a * b = {result}"
                        f" NO pertenece a Z{self.n}"
            )

        return PropertyResult(
            name = "Clausura bajo el producto",
            is_valid = True,
            explanation = f"Se verifico que para todos los pares (a, b) pertenecientes a Z{self.n},"
                    f" a * b (mod n) tambien pertenece a Z{self.n}"
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
            explanation = f"Se verifico que para todas las ternas (a, b, c) pertenecientes a Z{self.n},"
                    " (a + b) + c es igual a a + (b + c)"
        )


    def _verify_multiplicative_associativity(self, a: int, b: int, c: int) -> PropertyResult:
        left: int = self.zn.multiply(self.zn.multiply(a, b), c)
        right: int = self.zn.multiply(a, self.zn.multiply(b, c))

        if not right == left:
            return PropertyResult(
                name = "Asociatividad bajo el producto",
                is_valid = False,
                explanation = f"Para a = {a}, b = {b} y c = {c}"
                        " (a * b) * c NO es igual a a * (b * c)"
            )

        return PropertyResult(
            name = "Asociatividad bajo el producto",
            is_valid = True,
            explanation = f"Para todo a, b, c pertenecientes a Z{self.n}"
                    " (a * b) * c es igual a a * (b * c)"
        )


    def _verify_multiplicative_commutativity(self, a: int, b: int) -> PropertyResult:
        right: int = self.zn.multiply(a, b)
        left: int = self.zn.multiply(b, a)

        if not right == left:
            return PropertyResult(
                name = "Conmutatividad para el producto",
                is_valid = False,
                explanation = f"Se encontro un a = {a} y b = {b} pertenecientes a Z{self.n} "
                        f"tal que a * b = {right} NO es igual a b * a = {left}"
            )

        return PropertyResult(
            name = "Conmutatividad para el producto",
            is_valid = True,
            explanation = f"Se verifico que para todo a, b pertenecientes a Z{self.n} "
                    "a * b = b * a"
        )
