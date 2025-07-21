
from dataclasses import dataclass
from camera import Camera
from points import PointCloud, Point
from colours import colour_to_tuple
from vectors import Vector2, vec2_to_tuple_float

import pygame as pg

def render_point_cloud(display_surface: pg.Surface, point_cloud: PointCloud) -> None: 
    for point in point_cloud.points:
        render_point(display_surface=display_surface, point=point)

def render_point(display_surface: pg.Surface, point: Point) -> None:
    # Temperary implementation of this:
    pg.draw.circle(
        surface=display_surface,
        color=colour_to_tuple(point.colour),
        center=vec2_to_tuple_float(Vector2(point.position.x * 50, point.position.y * 50) + Vector2(200, 100)),
        radius=point.radius * 100,
    )