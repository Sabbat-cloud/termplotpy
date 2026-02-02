import termplotpy
import random

def barnsley_fern(n=5000):
    points = []
    x, y = 0.0, 0.0
    for _ in range(n):
        r = random.random()
        if r < 0.01:
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        points.append((x, y))
    return points

def main():
    width, height = 60, 30
    plotter = termplotpy.Plotter(width, height)
    
    print("Generando Fractal (Barnsley Fern)...")
    puntos = barnsley_fern(8000)
    
    # El fractal crece entre x:[-2.18, 2.65] y y:[0, 9.99]
    plotter.draw_axes(-3, 3, 0, 11)
    plotter.scatter(puntos, "green")
    plotter.draw_text("Barnsley Fern Fractal", 0.3, 0.95, "white")
    
    print(plotter.render())

if __name__ == "__main__":
    main()
