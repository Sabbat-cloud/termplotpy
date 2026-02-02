import termplotpy
import numpy as np
import time
import sys

def generate_initial_state(width, height, density=0.25):
    return np.random.choice([0, 1], size=(height, width), p=[1 - density, density])

def update_game_of_life(board):
    board_pad = np.pad(board, 1, mode='wrap')
    neighbors = (
        board_pad[0:-2, 0:-2] + board_pad[0:-2, 1:-1] + board_pad[0:-2, 2:] +
        board_pad[1:-1, 0:-2]                         + board_pad[1:-1, 2:] +
        board_pad[2:  , 0:-2] + board_pad[2:  , 1:-1] + board_pad[2:  , 2:]
    )
    return np.where((board == 1) & ((neighbors < 2) | (neighbors > 3)), 0,
           np.where((board == 0) & (neighbors == 3), 1, board))

def main():
    # Bajamos la altura a 18 para asegurar que no toque el borde de la terminal
    width, height = 70, 18 
    plotter = termplotpy.Plotter(width, height)
    
    board = generate_initial_state(width, height)
    generation = 0

    # 1. Limpiar pantalla completa (\033[2J)
    # 2. Ir a arriba a la izquierda (\033[H)
    # 3. Esconder cursor (\033[?25l)
    sys.stdout.write("\033[2J\033[H\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            plotter.clear()
            plotter.draw_axes(0, width, 0, height)
            
            rows, cols = np.where(board == 1)
            live_pixels = list(zip(cols.astype(float), rows.astype(float)))
            plotter.draw_pixels(live_pixels, "green")
            
            # --- RENDERIZADO ---
            output = plotter.render()
            
            # TÉCNICA DEFINITIVA: 
            # Volvemos a 0,0 (\033[H) ANTES de imprimir cada frame.
            # Imprimimos el frame y añadimos espacios al final de cada línea si fuera necesario
            # Pero lo más importante es el \033[H
            
            sys.stdout.write("\033[H") 
            sys.stdout.write(output)
            sys.stdout.write(f"\nGEN: {generation} | CELLS: {len(live_pixels)}    ") # Espacios extra para limpiar rastro
            sys.stdout.flush()

            board = update_game_of_life(board)
            generation += 1
            time.sleep(0.05)

    except KeyboardInterrupt:
        # Mostrar cursor al salir
        sys.stdout.write("\033[?25h\n")
        print("Simulación terminada.")

if __name__ == "__main__":
    main()
