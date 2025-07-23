
from dataclasses import dataclass
import moderngl as mgl
import numpy as np

@dataclass
class Mesh:
    program: mgl.Program
    layout: tuple[str, ...]
    vertices: list[float]
    vbo: mgl.Buffer = mgl.Buffer
    vao: mgl.VertexArray = mgl.VertexArray

def rebuild_vertex_buffer(ctx: mgl.Context, mesh: Mesh):
    mesh.vbo = ctx.buffer(np.array(mesh.vertices, dtype='f'))
    mesh.vao = ctx.vertex_array(mesh.program, [(mesh.vbo, *mesh.layout)])

def render_mesh(ctx: mgl.Context, mesh: Mesh, mode: int):
    mesh.vao.render(mode=mode)
