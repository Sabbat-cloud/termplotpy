import termplotpy
import numpy as np
import math
import time

def main():
    p = termplotpy.Plotter(80, 20)
    t = 0
    
    print("\033[2J\033[H")
    
    try:
        while True:
            p.clear()
            p.draw_grid(10, 5, 30, 30, 30)
            p.draw_axes(0, 10, -2, 2)
            
            # Simular señal de audio (Suma de senoides)
            x = np.linspace(0, 10, 160, dtype=np.float64)
            y = (np.sin(x + t) + 
                 0.5 * np.sin(2.5 * x + t * 1.5) + 
                 0.2 * np.sin(5.0 * x - t))
            
            # Enviar a Rust (NumPy optimizado)
            p.line_chart_np(x, y, "cyan")
            p.draw_text(f"OSCILLOSCOPE MODE - T:{t:.1f}", 0.3, 0.9, "white")
            
            print("\033[H" + p.render())
            t += 0.2
            time.sleep(0.04)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
