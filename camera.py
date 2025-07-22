
from dataclasses import dataclass

from vectors import Vector3, Vector2
from matrices import Matrix4, matrix4_mult
from math import sin, cos
import pygame as pg

OFFSET = Vector2(480, 270)
MOUSE_SENSITIVITY = 0.05
CAMERA_SPEED = 4

@dataclass
class Camera:
    position: Vector3
    pitch: float
    yaw: float
    roll: float

    focal: float = 1000
    camera_matrix: Matrix4 = Matrix4

def camera_movement(dt: float, camera: Camera, keys: list[bool], mouse_vel: Vector2) -> None:
    # Moving forwards and backwards
    if keys[pg.K_w]:
        camera.position.x += CAMERA_SPEED * sin(camera.yaw) * dt
        camera.position.z += CAMERA_SPEED * cos(camera.yaw) * dt
    if keys[pg.K_s]:
        camera.position.x -= CAMERA_SPEED * sin(camera.yaw) * dt
        camera.position.z -= CAMERA_SPEED * cos(camera.yaw) * dt
    # Moving sideways
    if keys[pg.K_d]:
        camera.position.x += CAMERA_SPEED * cos(camera.yaw) * dt
        camera.position.z -= CAMERA_SPEED * sin(camera.yaw) * dt
    if keys[pg.K_a]:
        camera.position.x -= CAMERA_SPEED * cos(camera.yaw) * dt
        camera.position.z += CAMERA_SPEED * sin(camera.yaw) * dt
    # Moving up and down
    if keys[pg.K_q]:
        camera.position.y += CAMERA_SPEED * dt
    if keys[pg.K_e]:
        camera.position.y -= CAMERA_SPEED * dt

    # Controlling camera rotation with mouse
    camera.yaw += mouse_vel.x * dt * MOUSE_SENSITIVITY
    camera.pitch -= mouse_vel.y * dt * MOUSE_SENSITIVITY

def calc_camera_matrix(camera: Camera) -> None:
    # Camera position
    camera.camera_matrix = Matrix4(elements=[
        1, 0, 0, -camera.position.x,
        0, 1, 0, -camera.position.y,
        0, 0, 1, -camera.position.z,
        0, 0, 0,                  1]
    )

    # Camera roll / Z
    camera.camera_matrix = matrix4_mult(
        Matrix4(elements=[
            cos(camera.roll), -sin(camera.roll), 0, 0,
            sin(camera.roll),  cos(camera.roll), 0, 0,
            0,                                0, 1, 0,
            0,                                0, 0, 1]
        ),
        camera.camera_matrix
    )

    # Camera yaw / Y
    camera.camera_matrix = matrix4_mult(
        Matrix4(elements=[
            cos(camera.yaw), 0, -sin(camera.yaw), 0,
            0,            1, 0,                   0,
            sin(camera.yaw), 0,  cos(camera.yaw), 0,
            0,               0,                0, 1]
        ),
        camera.camera_matrix
    )

    # Camera pitch / X
    camera.camera_matrix = matrix4_mult(
        Matrix4(elements=[
            1,                 0,                  0, 0,
            0, cos(camera.pitch), -sin(camera.pitch), 0,
            0, sin(camera.pitch),  cos(camera.pitch), 0,
            0,                 0,                  0, 1]
        ),
        camera.camera_matrix
    )
    
    # Camera Projection
    camera.camera_matrix = matrix4_mult(
        Matrix4(elements=[
            camera.focal,            0, 0, 0,
            0,            camera.focal, 0, 0,
            0,                       0, 0, 0,
            0,                       0, 1, 0]
        ),
        camera.camera_matrix
    )
    
    # Display Offset
    camera.camera_matrix = matrix4_mult(
        Matrix4(elements=[
            1,  0, 0, OFFSET.x,
            0, -1, 0, OFFSET.y,
            0,  0, 1,        0,
            0,  0, 0,        1]
        ),
        camera.camera_matrix
    )
    
    