import termplotpy
import math

def lorenz_attractor(n=500):
    """Genera puntos de un sistema caótico de Lorenz."""
    dt = 0.01
    x, y, z = 0.1, 0.0, 0.0
    s, r, b = 10.0, 28.0, 2.667
    points = []
    for _ in range(n):
        dx = s * (y - x) * dt
        dy = (x * (r - z) - y) * dt
        dz = (x * y - b * z) * dt
        x += dx
        y += dy
        z += dz
        # Proyectamos X y Z para verlo en 2D
        points.append((x, z))
    return points

def demo():
    # --- EJEMPLO 1: CAOS (Atractor de Lorenz) ---
    print("\n\033[1;33m[1] Atractor de Lorenz (Caos matemático)\033[0m")
    p1 = termplotpy.Plotter(60, 20)
    puntos_caos = lorenz_attractor(1000)
    
    # Usamos draw_axes con los límites aproximados del atractor
    p1.draw_axes(-20, 20, 0, 50)
    p1.line_chart(puntos_caos, "yellow")
    p1.draw_text("Lorenz Attractor", 0.3, 0.95, "white")
    print(p1.render())

    # --- EJEMPLO 2: INTERFERENCIA DE ONDAS ---
    print("\n\033[1;36m[2] Interferencia de Ondas (Patrón de batido)\033[0m")
    p2 = termplotpy.Plotter(80, 15)
    p2.draw_grid(10, 5, 40, 40, 40)
    
    onda = []
    for i in range(160):
        x = i * 0.1
        # Suma de dos senos con frecuencias cercanas
        y = math.sin(x) + math.sin(x * 1.1)
        onda.append((x, y))
        
    p2.draw_axes(0, 16, -2, 2)
    p2.line_chart(onda, "cyan")
    p2.draw_text("Wave Interference", 0.35, 0.1, "cyan")
    print(p2.render())

if __name__ == "__main__":
    demo()
