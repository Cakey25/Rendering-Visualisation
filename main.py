
from camera import Camera
from window import Display, create_display

from vectors import Vector3, Vector2
from dataclasses import fields
'''
@dataclass
class Test:
    name: str

    @property
    def double(self):
        return self.name + self.name

def main():

    test = Test('word')
    print(test.name)

    print(test.double)
'''

'''
DISPLAY_SIZE = Vector2(960, 540)

def main():

    display: Display = create_display(DISPLAY_SIZE)

    # Create a camera
    camera = Camera(
        position=Vector3(0, 0, 0),
        pitch=0,
        yaw=0,
    )

    while display.active:
'''

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
        for field in fields(col):
            print(field)
            value = getattr(col, field.name)
            setattr(col, field.name, clamp_int(num=value, lower=0, upper=255))
        return colour
    return wrapper

@validate_colour
@dataclass
class Colour:
    r: int
    g: int
    b: int
    a: int = 255

col = Colour(
    r=200,
    g=100,
    b=0,
)

print(col.r, col.g, col.b)
#main()
