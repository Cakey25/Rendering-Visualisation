
from dataclasses import dataclass
from camera import Camera
from points import PointCloud
from window import Display
from renderer import render_point_cloud

import pygame as pg

@dataclass
class Scene:
    display: Display
    objects: list[object]
    cameras: list[Camera]
    selected_camera: int = 0

def update_scene(scene: Scene) -> None:
    pass

def render_scene(scene: Scene) -> None:
    
    for scene_object in scene.objects:
        match scene_object:
            case PointCloud():
                render_point_cloud(scene.display.surface, scene_object)
            case _:
                pass

