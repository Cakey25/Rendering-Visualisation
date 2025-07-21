
from camera import Camera
from points import PointCloud, Point
from colours import colour_to_tuple
from vectors import Vector2, vec2_to_tuple_float, Vector3, Vector4
from matrices import matrix4_dot_vector4

import pygame as pg

def render_point_cloud(display_surface: pg.Surface, camera: Camera, point_cloud: PointCloud) -> None: 
    for point in point_cloud.points:
        render_point(display_surface=display_surface, camera=camera, point=point)

def render_point(display_surface: pg.Surface, camera: Camera, point: Point) -> None:
    # Temperary implementation of this:
    vertex = matrix4_dot_vector4(
        matrix=camera.camera_matrix.elements, 
        vector=point.position
    )

    if vertex == False:
        return
    
    pg.draw.circle(
        surface=display_surface,
        color=colour_to_tuple(point.colour),
        center=vec2_to_tuple_float(vertex),
        radius=point.radius * 100,
    )
'''
def vertex_transformation(camera: Camera, vertex: Vector4):
    pass
'''