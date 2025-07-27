
from camera import Camera
from window import Display, create_display, close_display, fill_display
from events import get_all_events, get_event
from vectors import Vector3, Vector2, vec2_to_tuple_int
from colours import Colour
from scene import Scene, render_scene, update_scene, get_active_camera
from points import generate_cube
from config import DISPLAY_SIZE, FPS
from shader_program import get_program
from mesh import Mesh, rebuild_vertex_buffer, render_mesh

from dataclasses import dataclass
import pygame as pg
import moderngl as mgl



BACKGROUND_COL = Colour(r=200, g=100, b=10)

def main() -> None:
    display: Display = create_display(DISPLAY_SIZE, pg.OPENGL | pg.DOUBLEBUF)

    # put this somewhere else
    ctx = mgl.create_context()
    ctx.gc_mode = 'auto'

    shader_program = get_program(ctx=ctx, name='quad')
    quad = Mesh(
        program=shader_program,
        layout=('2f', 'vert')
    )
    rebuild_vertex_buffer(
        ctx=ctx,
        mesh=quad, 
        vertices=[
            -0.5, -0.5,
            0.5, -0.5,
            -0.5, 0.5,
            -0.5, 0.5,
            0.5, -0.5,
            0.5, 0.5]
    )
        
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
        ctx.clear()

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

        render_mesh(mesh=quad, mode=mgl.TRIANGLES)

        pg.display.flip()

    close_display()

if __name__ == '__main__':
    main()
'''
create a 3d object class or something along those lines
the object will have a vbo and vao and later will have an option to do groups of objects in
a single vao and vbo,
the vertices will be sent into a shader which will be updated and stuff by a seperate thing
and the shader will have access to the normal, z value and coordinates and colour of each vertex
and will render the thing using the passed in camera matrix
will then render onto the screen


fto create a circle willl need a function that adds to a buffer for more vertices
depending on a center and a radius for a quad and will then render that thing using a circle shader
that will take 0.5 away from the uv and then do distance squared on it to see how big it is, could
then set the size depending on the z when applying the matrix to it.


'''
