import termplotpy
import numpy as np
import psutil
import time
import os

def main():
    width, height = 80, 15
    plotter = termplotpy.Plotter(width, height)
    
    # Historial de datos (últimos 80 puntos)
    cpu_history = np.zeros(width, dtype=np.float64)
    ram_history = np.zeros(width, dtype=np.float64)
    x_axis = np.arange(width, dtype=np.float64)

    print("\033[2J") # Limpiar pantalla inicial

    try:
        while True:
            # 1. Capturar datos reales
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent
            
            # 2. Actualizar arrays (desplazar a la izquierda y añadir nuevo al final)
            cpu_history = np.roll(cpu_history, -1)
            cpu_history[-1] = cpu_usage
            ram_history = np.roll(ram_history, -1)
            ram_history[-1] = ram_usage

            # 3. Dibujar
            plotter.clear()
            plotter.draw_grid(10, 5, 50, 50, 50)
            plotter.draw_axes(0, width, 0, 100)
            
            # Usamos el nuevo método optimizado para NumPy
            plotter.line_chart_np(x_axis, cpu_history, "cyan")
            plotter.line_chart_np(x_axis, ram_history, "magenta")
            
            plotter.draw_text(f"CPU: {cpu_usage}% (Cyan)", 0.05, 0.9, "cyan")
            plotter.draw_text(f"RAM: {ram_usage}% (Magenta)", 0.55, 0.9, "magenta")

            # 4. Mostrar y rebobinar
            output = plotter.render()
            # Mover cursor al inicio (0,0) para refresco limpio
            print("\033[H" + output) 
            
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitor finalizado.")

if __name__ == "__main__":
    main()
