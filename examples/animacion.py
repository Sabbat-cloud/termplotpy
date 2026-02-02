import termplotpy
import math
import time
import sys

def main():
    width = 60
    height = 15
    plotter = termplotpy.Plotter(width, height)
    
    phase = 0.0
    # Líneas a rebobinar: altura del canvas + bordes (2) + línea de info (1)
    lines_to_rewind = height + 2 + 1 

    print("\n\033[1;37;41m ANIMACIÓN PRO DESDE PYTHON \033[0m")
    print("Renderizando... (Ctrl+C para salir)")
    time.sleep(1)

    try:
        while True:
            # 1. Limpiar canvas interno
            plotter.clear()

            # 2. Dibujar fondo (Rejilla y Ejes)
            plotter.draw_grid(10, 4, 60, 60, 60)
            plotter.draw_axes(0.0, 10.0, -1.5, 1.5)

            # 3. Calcular puntos de las funciones (Lógica en Python)
            # Función 1: Cyan
            puntos_1 = []
            for i in range(120):
                x = i * (10.0 / 120.0)
                y = math.sin(x + phase) * math.cos(x * 0.5)
                puntos_1.append((x, y))
            
            # Función 2: Magenta
            puntos_2 = []
            for i in range(120):
                x = i * (10.0 / 120.0)
                y = (math.cos(x - phase * 1.5) * 0.5) - 0.5
                puntos_2.append((x, y))

            # 4. Enviar puntos al motor de Rust
            plotter.line_chart(puntos_1, "cyan")
            plotter.line_chart(puntos_2, "magenta")
            
            # 5. Texto
            plotter.draw_text("Sistema Dual Py", 0.40, 0.9, "yellow")

            # 6. Renderizar
            output = plotter.render()
            sys.stdout.write(output + "\n")
            sys.stdout.write(f"Phase: {phase:.2f} | Engine: Rust | TUI: Python\n")
            sys.stdout.flush()

            # 7. Pausa y Rebobinado del cursor (ANSI Escape Codes)
            time.sleep(0.05)
            sys.stdout.write(f"\033[{lines_to_rewind}A")
            
            phase += 0.1

    except KeyboardInterrupt:
        # Bajar el cursor al final para no romper la terminal al salir
        print("\n" * lines_to_rewind)
        print("Animación detenida.")

if __name__ == "__main__":
    main()
