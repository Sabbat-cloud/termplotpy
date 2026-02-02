import termplotpy
import numpy as np
import time
import sys

def main():
    plotter = termplotpy.Plotter(70, 15)
    num_bars = 70
    
    print("\033[2J\033[H") # Limpiar pantalla
    
    try:
        while True:
            plotter.clear()
            # Crear datos de "frecuencia" aleatorios suavizados
            data = np.random.uniform(0, 100, num_bars)
            x_axis = np.arange(num_bars, dtype=np.float64)
            
            # Dibujamos varias capas para efecto de degradado
            plotter.line_chart_np(x_axis, data, "yellow")
            plotter.draw_text("DYNAMIC EQUALIZER SIMULATION", 0.3, 0.9, "yellow")
            
            output = plotter.render()
            sys.stdout.write("\033[H" + output)
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDemo finalizada.")

if __name__ == "__main__":
    main()
