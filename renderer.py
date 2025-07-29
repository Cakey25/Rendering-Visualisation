
from camera import Camera
from points import PointCloud, Point
from colours import colour_to_tuple
from vectors import Vector2, vec2_to_tuple_float, Vector3, Vector4, vec4_to_vec2
from matrices import matrix4_dot_vector4
from mesh import Mesh, append_vertex_buffer

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

# This is specifically rendering circles at points so need to find a way to organise these functions
def update_mesh_buffer(camera: Camera, mesh: Mesh, vertex_length: int) -> None:
    for i in range(int(len(mesh.vertices) / vertex_length)):
        x = mesh.vertices[i * vertex_length + 0]
        y = mesh.vertices[i * vertex_length + 1]
        z = mesh.vertices[i * vertex_length + 2]

        transformed_vertex = vertex_transformation(
            camera=camera,
            position=Vector3(x, y, z)
        )
        if transformed_vertex is None:
            return
        centerx = transformed_vertex.x
        centery = transformed_vertex.y
        quad_vertices = generate_quad_mesh(center=transformed_vertex, width=0.1, height=0.1)
        append_vertex_buffer(mesh=mesh, vertices=quad_vertices, update_vertices=False)

def generate_quad_mesh(center: Vector2, width: float, height: float) -> list[float]:
    w = width / 2
    h = height / 2
    return [
        center.x - w, center.y - h,
        center.x + w, center.y - h,
        center.x - w, center.y + h,
        center.x - w, center.y + h,
        center.x + w, center.y - h,
        center.x + w, center.y + h
    ]
