import glfw
import numpy as np
import imageio
from OpenGL.GL import *

WIDTH, HEIGHT = 800, 600
MAX_DEPTH = 5

class Sphere:
    def __init__(self, center, radius, color):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color)

    def intersect(self, ray_origin, ray_direction):
        oc = ray_origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2.0 * np.dot(oc, ray_direction)
        c = np.dot(oc, oc) - self.radius**2
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            t1 = (-b - np.sqrt(discriminant)) / (2*a)
            t2 = (-b + np.sqrt(discriminant)) / (2*a)
            return min(t1, t2) if t1 > 0 else max(t1, t2)
        else:
            return None

class RayTracer:
    def __init__(self):
        self.objects = [
            Sphere(center=[0, 0, -5], radius=1, color=[255, 0, 0]),
            Sphere(center=[2, 1, -5], radius=1, color=[0, 0, 255])
        ]

    def trace_ray(self, origin, direction, depth=0):
        if depth > MAX_DEPTH:
            return np.zeros(3, dtype=np.uint8)

        hit_obj = None
        hit_distance = float('inf')

        for obj in self.objects:
            t = obj.intersect(origin, direction)
            if t is not None and t < hit_distance:
                hit_obj = obj
                hit_distance = t

        if hit_obj is not None:
            hit_point = origin + direction * hit_distance
            normal = (hit_point - hit_obj.center) / np.linalg.norm(hit_point - hit_obj.center)
            light_direction = np.array([1, 1, 1]) / np.linalg.norm(np.array([1, 1, 1]))

            # Lambertian shading
            intensity = max(0, np.dot(normal, light_direction))
            color = np.multiply(hit_obj.color, intensity)

            return color

        return np.zeros(3, dtype=np.uint8)

    def render(self):
        image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                ray_origin = np.array([x - WIDTH/2, HEIGHT/2 - y, 0])
                ray_direction = np.array([0, 0, -1])

                color = self.trace_ray(ray_origin, ray_direction)
                image[y, x] = color

        return image

def main():
    if not glfw.init():
        return

    window = glfw.create_window(WIDTH, HEIGHT, "Ray Tracer with GLFW", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    ray_tracer = RayTracer()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        rendered_image = ray_tracer.render()

        # Display the rendered image using the GLFW window
        gl_draw_image(rendered_image)

        glfw.swap_buffers(window)

    glfw.terminate()

def gl_draw_image(image):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRasterPos2f(-1, 1)
    glDrawPixels(image.shape[1], image.shape[0], GL_RGB, GL_UNSIGNED_BYTE, image.tobytes())

if __name__ == "__main__":
    main()
