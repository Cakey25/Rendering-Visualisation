
import pygame as pg
import sys

from dataclasses import dataclass
from vectors import Vector2, vec2_to_tuple_int
from colours import Colour, colour_to_tuple

@dataclass
class Display:
    size: Vector2
    surface: pg.Surface
    clock: pg.Clock
    active: bool

def create_display(display_size: Vector2, flags: int) -> Display:

    return Display(
        size=display_size,
        surface=pg.display.set_mode(vec2_to_tuple_int(display_size), flags),
        clock=pg.Clock(),
        active=True,
    )

def close_display() -> None:
    pg.quit()
    sys.exit()


def fill_display(surface: pg.Surface, colour: Colour) -> None:
    surface.fill(colour_to_tuple(colour=colour))
