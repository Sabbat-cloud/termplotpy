import termplotpy
import time
import sys

def main():
    # Usamos las mismas dimensiones seguras que en el Juego de la Vida
    width, height = 70, 18 
    plotter = termplotpy.Plotter(width, height)
    
    # 1. Limpiar pantalla completa (\033[2J)
    # 2. Ir a arriba a la izquierda (\033[H)
    # 3. Esconder cursor (\033[?25l)
    sys.stdout.write("\033[2J\033[H\033[?25l")
    sys.stdout.flush()

    try:
        max_iterations = 10
        # El fractal se vuelve más nítido conforme suben las iteraciones
        while max_iterations <= 150:
            plotter.clear()
            
            # Llamada al motor de Rust (Cálculo intensivo)
            start_time = time.time()
            plotter.draw_mandelbrot(max_iterations, "cyan")
            end_time = time.time()
            
            calc_ms = (end_time - start_time) * 1000
            
            # --- RENDERIZADO ---
            output = plotter.render()
            
            # Volvemos a 0,0 (\033[H) antes de escribir para sobreescribir exacto
            sys.stdout.write("\033[H")
            sys.stdout.write(output)
            # Línea de estado con espacios al final para limpiar rastro anterior
            sys.stdout.write(f"\nITER: {max_iterations} | RUST CALC: {calc_ms:.2f}ms    ")
            sys.stdout.flush()
            
            max_iterations += 2
            # Un pequeño delay para que el ojo humano aprecie el refinamiento
            time.sleep(0.03)
            
    except KeyboardInterrupt:
        # Restaurar cursor al salir
        sys.stdout.write("\033[?25h\n")
        print("Fractal detenido.")

if __name__ == "__main__":
    main()
