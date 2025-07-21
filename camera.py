
from dataclasses import dataclass

from vectors import Vector3
from matrices import Matrix4, identity_matrix4

@dataclass
class Camera:
    position: Vector3
    pitch: float
    yaw: float

    camera_matrix: Matrix4 = Matrix4

def calc_camera_matrix(camera: Camera):
    
    # calculate camera stuff

    camera.camera_matrix = identity_matrix4()
