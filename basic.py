import glfw
from OpenGL.GL import *
import numpy as np

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "OpenGL Triangle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Define vertices and colors for a triangle
    vertices = np.array([
        0.0, 0.6,  # Vertex 1
       -0.6, -0.6,  # Vertex 2
        0.6, -0.6   # Vertex 3
    ], dtype='f4')

    colors = np.array([
        1.0, 0.0, 0.0,  # Color for Vertex 1 (red)
        0.0, 1.0, 0.0,  # Color for Vertex 2 (green)
        0.0, 0.0, 1.0   # Color for Vertex 3 (blue)
    ], dtype='f4')

    # Create Vertex Buffer Objects (VBOs)
    vbo_position = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_position)
    glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

    vbo_color = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_color)
    glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)

    # Create a Vertex Array Object (VAO)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo_position)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, vbo_color)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(1)

    # Main loop
    while not glfw.window_should_close(window):
        # Render here, e.g., clear the buffer
        glClear(GL_COLOR_BUFFER_BIT)

        # Use our shader program
        glUseProgram(0)

        # Draw the triangle
        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Cleanup
    glfw.terminate()

if __name__ == "__main__":
    main()
