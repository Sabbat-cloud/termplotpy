import termplotpy
import numpy as np
import time
import sys

def main():
    width, height = 70, 20
    plotter = termplotpy.Plotter(width, height)
    world = np.zeros((height, width), dtype=int)
    
    sys.stdout.write("\033[2J\033[H\033[?25l")

    try:
        while True:
            # 1. Añadir agua en la parte superior central
            if np.random.random() > 0.3:
                world[0, width//2] = 1
            
            # 2. Física de partículas (de abajo hacia arriba para evitar saltos)
            new_world = world.copy()
            for y in range(height - 2, -1, -1):
                for x in range(width):
                    if world[y, x] == 1:
                        # Si abajo está vacío, cae
                        if world[y+1, x] == 0:
                            new_world[y, x] = 0
                            new_world[y+1, x] = 1
                        # Si no, intenta resbalar a los lados
                        else:
                            side = np.random.choice([-1, 1])
                            nx = x + side
                            if 0 <= nx < width and world[y+1, nx] == 0:
                                new_world[y, x] = 0
                                new_world[y+1, nx] = 1
            world = new_world

            # 3. Renderizado
            plotter.clear()
            plotter.draw_axes(0, width, 0, height)
            
            rows, cols = np.where(world == 1)
            points = [(float(c), float(height - r)) for r, c in zip(rows, cols)]
            plotter.draw_pixels(points, "cyan")
            
            sys.stdout.write("\033[H" + plotter.render() + f"\nWATER PHYSICS | PARTICLES: {len(points)}    ")
            sys.stdout.flush()
            time.sleep(0.02)

    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\n")
        print("Simulación de fluidos detenida.")

if __name__ == "__main__":
    main()
