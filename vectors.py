
from dataclasses import dataclass, astuple

@dataclass
class Vector2:
    x: float
    y: float
    
    def __iter__(self) -> iter:
        return iter((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f'Invalid parameter for add [{type(other)}]')

    def __radd__(self, other):
        self.__add__(other, self)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f'Invalid parameter for sub [{type(other)}]')
        
    def __rsub__(self, other):
        self.__sub__(other, self)
'''
    def __mul__(self, other):
        pass
'''
    
@dataclass
class Vector3:
    x: float
    y: float
    z: float

    def __iter__(self) -> iter:
        return iter((self.x, self.y, self.z))

@dataclass
class Vector4:
    x: float
    y: float
    z: float
    w: float = 0

def vec2_to_tuple_int(vector: Vector2) -> tuple[int, int]:
    return (round(vector.x), round(vector.y))

def vec3_to_tuple_int(vector: Vector3) -> tuple[int, int, int]:
    return (round(vector.x), round(vector.y), round(vector.z))
    
def vec2_to_tuple_float(vector: Vector2) -> tuple[float, float]:
    return (vector.x, vector.y)

def vec3_to_tuple_float(vector: Vector3) -> tuple[float, float, float]:
    return (vector.x, vector.y, vector.z)