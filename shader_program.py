
import moderngl as mgl

def get_program(ctx: mgl.Context, name: str):
    
    with open(f'shaders/{name}.vert', 'r') as file:
        vertex_shader = file.read()
    with open(f'shaders/{name}.frag', 'r') as file:
        fragment_shader = file.read()

    return ctx.program(
        vertex_shader=vertex_shader,
        fragment_shader=fragment_shader
    )