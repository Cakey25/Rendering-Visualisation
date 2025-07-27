
from dataclasses import dataclass
import moderngl as mgl
import numpy as np

@dataclass
class Mesh:
    program: mgl.Program
    layout: tuple[str, ...]
    vertices: list[float] = list[float]
    vbo: mgl.Buffer = mgl.Buffer
    vao: mgl.VertexArray = mgl.VertexArray
    offset: int = 0
    size: int = 0

def build_empty_buffer(ctx: mgl.Context, mesh: Mesh, size: int) -> None:
    mesh.vertices = []
    mesh.vbo = ctx.buffer(np.zeros(shape=size, dtype='f'))
    mesh.vao = ctx.vertex_array(mesh.program, [(mesh.vbo, *mesh.layout)])
    mesh.offset = 0
    mesh.size = size * 4

def update_vertex_buffer(mesh: Mesh, vertices: list[float]) -> None:
    size = len(vertices) * 4
    if size > mesh.size:
        raise ValueError(f'Buffer is too small: {mesh.size} bytes for vertices of size: {size} bytes')
    vertices = vertices
    mesh.vbo.write(data=np.array(vertices, dtype='f'), offset=0)
    mesh.offset = size

def append_vertex_buffer(mesh: Mesh, vertices: list[float]) -> None:
    size = len(vertices) * 4 + mesh.offset
    if size > mesh.size:
        raise ValueError(f'Buffer is too small: {mesh.size} bytes for vertices of size: {size} bytes')
    mesh.vertices += vertices
    mesh.vbo.write(data=np.array(vertices, dtype='f'), offset=mesh.offset)
    mesh.offset += len(vertices) * 4

def rebuild_vertex_buffer(ctx: mgl.Context, mesh: Mesh, vertices: list[float]) -> None:
    mesh.vertices = vertices
    mesh.vbo = ctx.buffer(np.array(mesh.vertices, dtype='f'))
    mesh.vao = ctx.vertex_array(mesh.program, [(mesh.vbo, *mesh.layout)])
    mesh.offset = len(vertices) * 4
    mesh.size = len(vertices) * 4

def render_mesh(mesh: Mesh, mode: int) -> None:
    mesh.vao.render(mode=mode)
