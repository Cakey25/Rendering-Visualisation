
from camera import Camera
from window import Display, create_display, close_display, fill_display
from events import get_all_events, get_event
from vectors import Vector3, Vector2
from colours import Colour

from dataclasses import dataclass
import pygame as pg

DISPLAY_SIZE = Vector2(960, 540)

def main():
    display: Display = create_display(DISPLAY_SIZE)
    '''
    # Create a camera
    camera = Camera(
        position=Vector3(0, 0, 0),
        pitch=0,
        yaw=0,
    )
    '''
    
    while display.active:
        event_flags: dict[int: bool] = get_all_events()

        if get_event(event=pg.QUIT, event_flags=event_flags) or get_event(event=pg.K_ESCAPE, event_flags=event_flags):
            display.active = False

        background_col = Colour(r=200, g=100, b=10)
        fill_display(surface=display.surface, colour=background_col)

        pg.display.flip()

    close_display()

if __name__ == '__main__':
    main()
