
import pygame as pg
import sys

from dataclasses import dataclass
from vectors import Vector2
from colours import Colour

@dataclass
class Display:
    size: Vector2
    surface: pg.Surface
    clock: pg.Clock
    active: bool

def create_display(display_size: Vector2) -> Display:

    return Display(
        size=display_size,
        surface=pg.display.set_mode(display_size.ituple),
        #display=pg.display.set_mode(size=(960, 540)),
        clock=pg.Clock(),
        active=True,
    )

def close_display() -> None:
    pg.quit()
    sys.exit()


def fill_display(surface: pg.Surface, colour: Colour) -> None:
    surface.fill(colour.tuple)
