```markdown
# termplotpy 🐍🦀

**Fast Terminal Data Visualization for Python, powered by Rust.**

`termplotpy` es una librería de gráficos para la terminal de alta densidad que utiliza caracteres **Unicode Braille** (2x4 puntos por celda) para ofrecer una resolución superior al ASCII tradicional.

---

## 🔥 ¿Por qué termplotpy?

- **Rendimiento de Rust**: El trazado de líneas y la rasterización de píxeles se realizan en memoria nativa.
- **Integración con NumPy**: Pasa arrays directamente al motor de Rust sin conversiones lentas.
- **TUI-First**: Diseñado específicamente para animaciones fluidas en la terminal (60 FPS+).
- **Colores Reales**: Soporte completo para TrueColor (RGB).

## 🚀 Instalación

```bash
# Requiere Rust instalado para compilar
git clone [https://github.com/tu_usuario/termplotpy](https://github.com/tu_usuario/termplotpy)
cd termplotpy
python -m venv .venv
source .venv/bin/activate
pip install maturin numpy psutil
maturin develop

```

## 🖼️ Showcase (Ejemplos incluidos)

1. **Monitor de Sistema**: Visualiza el uso de CPU y RAM en tiempo real usando NumPy.
2. **Juego de la Vida**: Una simulación de Conway fluida usando el motor de píxeles discretos.
3. **Fractales**: Renderiza el Helecho de Barnsley con miles de puntos instantáneamente.
4. **Física y Caos**: Explora el Atractor de Lorenz y patrones de interferencia de ondas.
5. **Animaciones**: Generadores de ondas complejas con rebobinado de cursor ANSI.

## 🛠 Ejemplo Rápido

```python
import termplotpy
import numpy as np

p = termplotpy.Plotter(60, 15)
x = np.linspace(0, 10, 100, dtype=np.float64)
y = np.sin(x)

p.line_chart_np(x, y, "cyan")
print(p.render())

```

---

Diseñado con ❤️ por Sabbat (Rust + Python Hybrid)

```
