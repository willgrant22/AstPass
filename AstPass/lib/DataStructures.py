from dataclasses import dataclass


# Dataclass to structure UI state
@dataclass(init=True, repr=False, eq=False, order=False, unsafe_hash=False, frozen=True)
class CurrentState:
    __slots__ = ['Length', 'Symbols', 'Numbers', 'Uppercase', 'Lowercase']
    Length: int
    Symbols: bool
    Numbers: bool
    Uppercase: bool
    Lowercase: bool


