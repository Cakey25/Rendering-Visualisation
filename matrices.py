
from dataclasses import dataclass
from vectors import Vector4, Vector2, Vector3

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

def matrix4_dot(m1: list[float], m2: list[float], row: int, col: int):
    result  = m1[0 + 4 * row] * m2[0  + col]
    result += m1[1 + 4 * row] * m2[4  + col]
    result += m1[2 + 4 * row] * m2[8  + col]
    result += m1[3 + 4 * row] * m2[12 + col]
    return result

def matrix4_mult(mat1: Matrix4, mat2: Matrix4):
    return Matrix4(elements=[
        matrix4_dot(mat1.elements, mat2.elements, index // 4, index % 4) for index in range(16)
    ])

# Fix this function as it is not very clear as what it is up to
def matrix4_dot_vector4(matrix: Matrix4, vector: Vector3) -> Vector2 | bool:
    vec4 = Vector4(vector.x, vector.y, vector.z, 1)
    result = Vector4(0, 0, 0, 0)
    result.x = matrix[0]  * vec4.x + matrix[1]  * vec4.y + matrix[2]  * vec4.z + matrix[3]  * vec4.w
    result.y = matrix[4]  * vec4.x + matrix[5]  * vec4.y + matrix[6]  * vec4.z + matrix[7]  * vec4.w
    result.z = matrix[8]  * vec4.x + matrix[9]  * vec4.y + matrix[10] * vec4.z + matrix[11] * vec4.w
    result.w = matrix[12] * vec4.x + matrix[13] * vec4.y + matrix[14] * vec4.z + matrix[15] * vec4.w

    if result.w > 0.01: 
        result.x = result.x / result.w
        result.y = result.y / result.w
        return Vector2(result.x, result.y)
    else:
        return False

