
from camera import Camera
from window import Display, create_display, close_display, fill_display
from events import get_all_events, get_event
from vectors import Vector3, Vector2, vec2_to_tuple_int
from colours import Colour
from scene import Scene, render_scene, update_scene, get_active_camera
from points import generate_cube
from config import DISPLAY_SIZE, FPS

from dataclasses import dataclass
import pygame as pg



BACKGROUND_COL = Colour(r=200, g=100, b=10)

def main() -> None:
    display: Display = create_display(DISPLAY_SIZE)
        
    # Creating scene - which will be done from json at some point
    scene = Scene(
        display=display,
        objects=[generate_cube(colour=Colour(255, 255, 255), radius=0.05)],
        cameras=[Camera(
            position=Vector3(0.5, 0.5, -1),
            pitch=0,
            yaw=0,
            roll=0)],
        selected_camera=0,
    )

    # Setup mouse
    pg.event.set_grab(True)
    pg.mouse.set_visible(False)
    pg.mouse.set_pos(vec2_to_tuple_int(DISPLAY_SIZE))
    
    dt: float = 0
    while display.active:

        # Make a inputs data class to contain these so i can pass it around
        event_flags: dict[int: bool] = get_all_events()
        keys: list[bool] = pg.key.get_pressed()

        mouse_vel = Vector2(*pg.mouse.get_rel())

        if get_event(event=pg.QUIT, event_flags=event_flags) or get_event(event=pg.K_ESCAPE, event_flags=event_flags):
            display.active = False

        fill_display(surface=display.surface, colour=BACKGROUND_COL)

        update_scene(dt=dt, scene=scene, keys=keys, mouse_vel=mouse_vel)

        render_scene(scene)

        dt: float = display.clock.tick(FPS) / 1_000

        pg.display.flip()

    close_display()

if __name__ == '__main__':
    main()
'''
# things to fix,
the offset in the other file,
camera movement with the mouse
the functions in the matrix file - clearer inputs and outputs and better error handling
way to draw lines between the dots
go through and do more type annotations
'''
