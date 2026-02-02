# termplotpy 🐍🦀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![Rust](https://img.shields.io/badge/rust-1.70+-orange.svg)](https://www.rust-lang.org)

**High-performance terminal graphics engine.** Renderiza fractales, fluidos y datos científicos a una velocidad nativa directamente en tu terminal.

`termplotpy` utiliza caracteres **Unicode Braille** para subdividir cada celda de la terminal en una matriz de 2x4, permitiendo una resolución efectiva mucho mayor que el ASCII art convencional.

---

## 📺 Demo en Vivo

![Ejemplo de funciones](assets/animacion.gif)
*Animación de ejemplo*

![Fuego Dinámico](assets/fuego.gif)
*Simulación de fluidos térmicos renderizada a 60 FPS.*

## 🚀 Puntos Clave

- **Hybrid Engine**: Lógica de alto nivel en Python, renderizado crítico en Rust via PyO3.
- **Braille Matrix**: Resolución de alta densidad (píxeles de 2x4 por carácter).
- **NumPy Native**: Soporte para `std::simd` implícito al pasar arrays de NumPy directamente a Rust.
- **Zero-Flicker**: Técnicas de posicionamiento absoluto de cursor para animaciones suaves.



---

## 📦 Instalación

Asegúrate de tener instalado el [Rust toolchain](https://rustup.rs/).

```bash
git clone [https://github.com/tu_usuario/termplotpy](https://github.com/tu_usuario/termplotpy)
cd termplotpy
python -m venv .venv
source .venv/bin/activate
pip install maturin numpy psutil
maturin develop --release

```

---

## 🕹️ Galería de Ejemplos (`/examples`)

Hemos incluido una suite de pruebas para demostrar la versatilidad del motor:

| Ejemplo | Descripción | Tecnología |
| --- | --- | --- |
| `mandelbrot.py` | Cálculo intensivo de fractales en tiempo real. | **Fuerza Bruta Rust** |
| `fuego.py` | Simulación de partículas de calor y propagación. | **Heatmap & TrueColor** |
| `agua.py` | Física de fluidos y colisiones de partículas. | **Física de Partículas** |
| `game_of_life.py` | El clásico de Conway optimizado con NumPy. | **Autómatas Celulares** |
| `monitor_cpu.py` | Dashboard de rendimiento del sistema. | **Integración NumPy** |
---

## 🛠️ Uso Básico

Crear un gráfico es tan sencillo como definir el lienzo y lanzar los datos:

```python
import termplotpy
import numpy as np

# Inicializar plotter (ancho, alto en caracteres)
p = termplotpy.Plotter(80, 20)

# Datos con NumPy
x = np.linspace(0, 10, 200, dtype=np.float64)
y = np.sin(x) * np.exp(-x/5)

# Dibujar ejes y línea
p.draw_axes(0, 10, -1, 1)
p.line_chart_np(x, y, "cyan")

# Renderizar en la terminal
print(p.render())

```

---

## 🧠 Arquitectura Técnica

El núcleo del proyecto separa la gestión de la memoria del lienzo (Rust) de la lógica de negocio (Python).

1. **BrailleCanvas (Rust)**: Gestiona un buffer de bits donde cada byte representa un bloque Braille.
2. **ChartContext (Rust)**: Proporciona primitivas geométricas (líneas, círculos, texto).
3. **PyO3 Bridge**: Realiza el mapeo de tipos de datos, permitiendo que Python acceda a punteros de memoria de Rust de forma segura.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes ideas para nuevos algoritmos de renderizado o optimizaciones en el bridge, abre un PR o una Issue.

---

Diseñado con ❤️ por **Sabbat** e impulsado por la velocidad de **Rust**.

```

---

