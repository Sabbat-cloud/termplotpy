import termplotpy
import numpy as np
import time
import sys

def main():
    width, height = 80, 25
    plotter = termplotpy.Plotter(width, height)
    
    # Matriz de calor (0 a 100)
    fire_map = np.zeros((height, width))
    
    sys.stdout.write("\033[2J\033[H\033[?25l")
    
    try:
        while True:
            # 1. Crear combustible en la base (línea inferior)
            fire_map[-1, :] = np.random.randint(80, 101, size=width)
            
            # 2. Propagar calor hacia arriba con enfriamiento aleatorio
            for y in range(height - 1):
                for x in range(width):
                    # El calor de un punto es el promedio de los de abajo
                    below = fire_map[(y + 1) % height, x]
                    decay = np.random.randint(0, 5)
                    fire_map[y, x] = max(0, below - decay)
            
            # 3. Dibujar en plotter
            plotter.clear()
            plotter.draw_axes(0, width, 0, height)
            
            rows, cols = np.where(fire_map > 10)
            points = []
            for r, c in zip(rows, cols):
                # Usamos diferentes colores según la intensidad (calor)
                intensity = fire_map[r, c]
                color = "yellow" if intensity > 70 else "red"
                points.append((float(c), float(height - r)))
                plotter.draw_pixels([(float(c), float(height - r))], color)

            output = plotter.render()
            sys.stdout.write("\033[H" + output + f"\nFLAME ENGINE | HEAT: {np.mean(fire_map):.2f}")
            sys.stdout.flush()
            time.sleep(0.03)
            
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\n")
        print("Fuego extinguido.")

if __name__ == "__main__":
    main()
