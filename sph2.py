import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
import numpy as np

def draw_sphere(radius=1.0, slices=30, stacks=30):
    for i in range(stacks):
        lat0 = np.pi * (-0.5 + (i / stacks))
        z0 = np.sin(lat0)
        zr0 = np.cos(lat0)

        lat1 = np.pi * (-0.5 + ((i + 1) / stacks))
        z1 = np.sin(lat1)
        zr1 = np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * np.pi * (j / slices)
            x = np.cos(lng)
            y = np.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glColor3f(1.0 - i / stacks, 1.0, i / stacks)  # Vertex color
            glVertex3f(radius * x * zr0, radius * y * zr0, radius * z0)

            glNormal3f(x * zr1, y * zr1, z1)
            glColor3f(1.0 - (i + 1) / stacks, 1.0, (i + 1) / stacks)  # Vertex color
            glVertex3f(radius * x * zr1, radius * y * zr1, radius * z1)

        glEnd()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Set light position and properties
    light_position = [1.0, 1.0, 1.0, 0.0]  # Directional light from the positive xyz axis
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "OpenGL Sphere with Lighting", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    setup_lighting()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 3, 1, 1)

        draw_sphere()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
