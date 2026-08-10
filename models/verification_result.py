from dataclasses import dataclass
from models.property_result import PropertyResult


@dataclass
class VerificationResult:


    n: int
    additive_group: PropertyResult
    multiplicative_semigroup: PropertyResult
    additive_abelian_group: PropertyResult
    ring: PropertyResult
    commutative_ring: PropertyResult
    field: PropertyResult
    additive_identity: int | None
    multiplicative_identity: int | None
    additive_inverses: dict[int, int]
    multiplicative_inverses: dict[int, int]
    addition_table: list[list[int]]
    multiplication_table: list[list[int]]