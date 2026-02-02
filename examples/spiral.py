import termplotpy
import math

def generar_espiral():
    puntos = []
    t = 0.0
    while t < 12.0 * math.pi:
        a, b = 0.1, 0.15
        r = a * math.exp(b * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        puntos.append((x, y))
        t += 0.05
    return puntos

# 1. Crear el plotter (60 columnas, 20 filas)
plotter = termplotpy.Plotter(60, 20)

# 2. Obtener los puntos
datos = generar_espiral()

# 3. Dibujar la serie en color cyan
plotter.line_chart(datos, "cyan")

# 4. Mostrar el resultado
print("\n--- ESPIRAL GENERADA DESDE PYTHON (RUST ENGINE) ---")
print(plotter.render())
