
from dataclasses import dataclass

def validate_matrix4(mat: object):
    def wrapper(*args, **kwargs):
        matrix4 = mat(*args, **kwargs)
        if len(matrix4.elements) == 16:
            return matrix4
        else:
            raise ValueError('Matrix4 does not have a length of 16 elements')
    return wrapper

@validate_matrix4
@dataclass
class Matrix4:
    elements: list[float]

def identity_matrix4() -> Matrix4:
    return Matrix4([
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1,
    ])
