This is my second attempt at a 3d renderer in python where I have handled all of the maths myself.
To try and get better a more functional and less OOP style, I only used data classes for this project.
This is so the code would be easier to replicate in a lower level language which is where much of this functionality would be.
I also tried to include type hints in all the places i could for this reason.

This is what the scene currently looks like at the time of writing (08/08/25):

<img width="954" height="565" alt="image" src="https://github.com/user-attachments/assets/0d248fb0-da33-4c8b-8a38-7bb41e5d2f1c" />

Although very simple and not looking great, this version is doing all the matrices calculations on the vertices of a cube to transform
them from world space into camera space and then these posisions are used to generate 8 quads that are put into a mesh and sent to the GPU
for rendering. In a furthre version I would like to move the camera matrix to the GPU side so that the GPU is responsible for all of the rendering.

The run this project run main.py, the only dependacies are moderngl, numpy and pygame.
To move the camera around you can use w,a,s,d for horizontal movement and q,e for vertical.
To move the rotation of the camera you can use the mouse.
