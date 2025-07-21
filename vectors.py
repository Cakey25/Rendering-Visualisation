
from dataclasses import dataclass, astuple

@dataclass
class Vector2:
    x: float
    y: float
    
    def __iter__(self) -> iter:
        return iter((self.x, self.y))

    @property 
    def ituple(self) -> tuple[int, int]:
        return (self.x, self.y)

@dataclass
class Vector3:
    x: float
    y: float
    z: float

    def __iter__(self) -> iter:
        return iter((self.x, self.y, self.z))

    @property 
    def integer(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)