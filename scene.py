
from dataclasses import dataclass
from camera import Camera, calc_camera_matrix, camera_movement
from points import PointCloud
from window import Display
from renderer import render_point_cloud
from vectors import Vector2

import pygame as pg

@dataclass
class Scene:
    display: Display
    objects: list[object]
    cameras: list[Camera]
    selected_camera: int = 0

def get_active_camera(scene: Scene) -> Camera:
    return scene.cameras[scene.selected_camera]

def update_scene(scene: Scene, keys: list[bool], dt: float, mouse_vel: Vector2) -> None:
    camera_movement(dt=dt, camera=get_active_camera(scene), keys=keys, mouse_vel=mouse_vel)
    calc_camera_matrix(camera=get_active_camera(scene))

def render_scene(scene: Scene) -> None:
    
    for scene_object in scene.objects:
        match scene_object:
            case PointCloud():
                render_point_cloud(
                    display_surface=scene.display.surface,
                    camera=get_active_camera(scene),
                    point_cloud=scene_object
                )
            case _:
                pass

