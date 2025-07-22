
from camera import Camera
from points import PointCloud, Point
from colours import colour_to_tuple
from vectors import Vector2, vec2_to_tuple_float, Vector3, Vector4, vec4_to_vec2
from matrices import matrix4_dot_vector4

import pygame as pg

def render_point_cloud(display_surface: pg.Surface, camera: Camera, point_cloud: PointCloud) -> None: 
    for point in point_cloud.points:
        render_point(display_surface=display_surface, camera=camera, point=point)

def render_point(display_surface: pg.Surface, camera: Camera, point: Point) -> None:
    # Get the location of the point on screen
    vertex = vertex_transformation(camera=camera, position=point.position)
    # Check if point is valid
    if vertex is None:
        return
    
    # Draw Circle
    pg.draw.circle(
        surface=display_surface,
        color=colour_to_tuple(point.colour),
        center=vec2_to_tuple_float(vertex),
        radius=point.radius * 100,
    )

def vertex_transformation(camera: Camera, position: Vector3) -> Vector2 | None:

    # Get point in projection space 
    vector = matrix4_dot_vector4(
        matrix=camera.camera_matrix.elements, 
        vector=Vector4(position.x, position.y, position.z, 1)
    )

    # If the vertex is in front of the camera, then correct x, y for the depth of vertex
    if vector.w > 0: 
        vector.x = vector.x / vector.w
        vector.y = vector.y / vector.w
        return vec4_to_vec2(vector=vector)
    else:
        return None