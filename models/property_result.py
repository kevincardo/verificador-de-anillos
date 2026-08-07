from dataclasses import dataclass


@dataclass
class PropertyResult:


    name: str
    is_valid: bool
    explanation: str