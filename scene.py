
from dataclasses import dataclass
from camera import Camera, calc_camera_matrix, camera_movement
from points import PointCloud
from window import Display, fill_display
from renderer import render_point_cloud
from vectors import Vector2
from shader_program import get_program
from mesh import Mesh, build_empty_buffer, update_vertex_buffer, append_vertex_buffer, render_mesh
from points import generate_cube
from colours import Colour

import pygame as pg
import moderngl as mgl

@dataclass
class Scene:
    display: Display
    cameras: list[Camera]
    # Each object name has a render order and and update order as well as pointer to object
    objects: dict[str: object] = dict
    selected_camera: int = 0

    def __post_init__(self) -> None:
        self.objects = dict()

def generate_scene(scene: Scene, ctx: mgl.Context) -> None:
    scene.objects['quad_program'] = get_program(ctx=ctx, name='quad')
    scene.objects['quad'] = Mesh(
        program=scene.objects['quad_program'],
        layout=('2f', 'vert')
    )
    # Create a empty buffer
    build_empty_buffer(ctx=ctx, mesh=scene.objects['quad'], size=12)
    # Set buffer to 1 triangle
    update_vertex_buffer(
        mesh=scene.objects['quad'], 
        vertices=[
            -0.5, -0.5,
            0.5, -0.5,
            -0.5, 0.5,
    ])
    # Append another triangle to buffer
    append_vertex_buffer(
        mesh=scene.objects['quad'],
        vertices=[
            -0.5, 0.5,
            0.5, -0.5,
            0.5, 0.5
    ])
    scene.objects['cube_vertices'] = generate_cube(
        colour=Colour(255, 255, 255),
        radius=0.2
    )

def get_active_camera(scene: Scene) -> Camera:
    return scene.cameras[scene.selected_camera]

def update_scene(scene: Scene, keys: list[bool], dt: float, mouse_vel: Vector2) -> None:
    camera_movement(dt=dt, camera=get_active_camera(scene), keys=keys, mouse_vel=mouse_vel)
    calc_camera_matrix(camera=get_active_camera(scene))

def render_scene(scene: Scene, surface: pg.Surface, ctx: mgl.Context) -> None:
    ctx.clear()
    fill_display(surface=surface, colour=Colour(0, 0, 0))
    
    render_point_cloud(
        display_surface=scene.display.surface,
        camera=get_active_camera(scene),
        point_cloud=scene.objects['cube_vertices']
    )

    render_mesh(mesh=scene.objects['quad'], mode=mgl.TRIANGLES)


