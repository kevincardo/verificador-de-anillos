from dataclasses import dataclass
from models.property_result import PropertyResult


@dataclass
class VerificationResult:


    additive_group: PropertyResult
    multiplicative_semigroup: PropertyResult
    distributivity: PropertyResult
    ring: PropertyResult
    commutative_ring: PropertyResult
    field: PropertyResult