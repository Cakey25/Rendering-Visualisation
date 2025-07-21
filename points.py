
from dataclasses import dataclass
from vectors import Vector3
from colours import Colour

@dataclass
class Point:
    position: Vector3
    colour: Colour = Colour
    radius: float = 0

@dataclass
class PointCloud:
    points: list[Point]

def generate_cube(colour: Colour, radius: float) -> PointCloud:
    cube = PointCloud(points=[
        Point(position=Vector3(0, 0, 0)),
        Point(position=Vector3(1, 0, 0)),
        Point(position=Vector3(0, 1, 0)),
        Point(position=Vector3(1, 1, 0)),
        Point(position=Vector3(0, 0, 1)),
        Point(position=Vector3(1, 0, 1)),
        Point(position=Vector3(0, 1, 1)),
        Point(position=Vector3(1, 1, 1)),
        ]
    )
    for point in cube.points:
        point.colour = colour
        point.radius = radius
    return cube
