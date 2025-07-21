
from dataclasses import dataclass

def clamp_int(num: int, lower: int, upper: int) -> int:
    if lower <= num <= upper:
        return num
    elif num < lower:
        return lower
    elif num > upper:
        return upper

def validate_colour(col: object):
    def wrapper(*args, **kwargs):
        colour = col(*args, **kwargs)
        colour.r = clamp_int(colour.r, 0, 255)
        colour.g = clamp_int(colour.g, 0, 255)
        colour.b = clamp_int(colour.b, 0, 255)
        colour.a = clamp_int(colour.a, 0, 255)
        return colour
    return wrapper

@validate_colour
@dataclass
class Colour:
    r: int
    g: int
    b: int
    a: int = 255

    def __iter__(self):
        return iter((self.r, self.g, self.b, self.a))
    
    @property
    def tuple(self):
        return (self.r, self.g, self.b, self.a)
