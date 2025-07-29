
from dataclasses import dataclass
from camera import Camera, calc_camera_matrix, camera_movement
from points import PointCloud
from window import Display, fill_display
from renderer import render_point_cloud, update_mesh_buffer
from vectors import Vector2
from shader_program import get_program
from mesh import Mesh, build_empty_buffer, update_vertex_buffer, append_vertex_buffer, render_mesh
from points import generate_cube
from colours import Colour

import pygame as pg
import moderngl as mgl
import numpy as np

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
    scene.objects['circle_program'] = get_program(ctx=ctx, name='quad')
    scene.objects['vertices'] = Mesh(
        program=scene.objects['circle_program'],
        layout=('2f', 'vert'),
        vertices=[
            0, 0, 0,
            1, 0, 0,
            0, 1, 0,
            1, 1, 0,
            0, 0, 1,
            1, 0, 1,
            0, 1, 1,
            1, 1, 1
    ])

def get_active_camera(scene: Scene) -> Camera:
    return scene.cameras[scene.selected_camera]

def update_scene(scene: Scene, ctx: mgl.Context, keys: list[bool], dt: float, mouse_vel: Vector2) -> None:
    camera_movement(dt=dt, camera=get_active_camera(scene), keys=keys, mouse_vel=mouse_vel)
    calc_camera_matrix(camera=get_active_camera(scene))
    # Create a empty buffer
    build_empty_buffer(ctx=ctx, mesh=scene.objects['vertices'], size=12*8, update_vertices=False)
    update_mesh_buffer(camera=get_active_camera(scene), mesh=scene.objects['vertices'], vertex_length=3)

    # Code to read a buffer
    vbo = list(np.frombuffer(scene.objects['vertices'].vbo.read(), dtype='f'))
    vbo_string = ''.join(
        [f'tri{i*2}:{vbo[i]} {vbo[i + 1]} {vbo[i + 2]},tri{i*2+1}:{vbo[i+3]} {vbo[i+4]} {vbo[i+5]}\n' 
        for i in range(int(len(vbo) / 6))])
    print(f'vbo:{vbo_string}')

def render_scene(scene: Scene, surface: pg.Surface, ctx: mgl.Context) -> None:
    ctx.clear(1, 1, 1)
    fill_display(surface=surface, colour=Colour(0, 0, 0))

    render_mesh(mesh=scene.objects['vertices'], mode=mgl.TRIANGLES)


