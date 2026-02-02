mod canvas;
mod charts;

use pyo3::prelude::*;
use charts::ChartContext;
use numpy::PyReadonlyArray1;
use colored::Color;

#[pyclass]
struct Plotter {
    ctx: ChartContext,
}

#[pymethods]
impl Plotter {
    #[new]
    fn new(width: usize, height: usize) -> Self {
        Self {
            ctx: ChartContext::new(width, height),
        }
    }
    fn draw_pixels(&mut self, points: Vec<(f64, f64)>, color_name: Option<&str>) {
        let color = parse_color(color_name);
        for (x, y) in points {
            // Convertir coordenadas del "juego" a coordenadas del canvas
            let (px, py) = self.ctx.normalize_coords(x, y);
            self.ctx.canvas.set_pixel(px as usize, py as usize, color);
        }
    }

    fn draw_mandelbrot(&mut self, max_iter: usize, color_name: Option<&str>) {
        let color = parse_color(color_name);
        let w_px = self.ctx.canvas.width * 2;
        let h_px = self.ctx.canvas.height * 4;
        
        // Rangos del plano complejo para Mandelbrot
        let x_min = -2.0; let x_max = 1.0;
        let y_min = -1.2; let y_max = 1.2;

        for py in 0..h_px {
            for px in 0..w_px {
                let x0 = x_min + (px as f64 / w_px as f64) * (x_max - x_min);
                let y0 = y_min + (py as f64 / h_px as f64) * (y_max - y_min);
                
                let mut x = 0.0;
                let mut y = 0.0;
                let mut iteration = 0;
                
                while x*x + y*y <= 4.0 && iteration < max_iter {
                    let xtemp = x*x - y*y + x0;
                    y = 2.0*x*y + y0;
                    x = xtemp;
                    iteration += 1;
                }
                
                if iteration == max_iter {
                    self.ctx.canvas.set_pixel(px, py, color);
                }
            }
        }
    }

    // --- MÉTODOS PARA NUMPY (Ultra rápidos) ---
    fn line_chart_np(&mut self, x: PyReadonlyArray1<f64>, y: PyReadonlyArray1<f64>, color_name: Option<&str>) {
        let x_view = x.as_array();
        let y_view = y.as_array();
        // Creamos los puntos combinando ambos arrays eficientemente
        let points: Vec<(f64, f64)> = x_view.iter().zip(y_view.iter())
            .map(|(&xi, &yi)| (xi, yi))
            .collect();

        let color = parse_color(color_name);
        self.ctx.line_chart(&points, color);
    }

    fn draw_grid(&mut self, cols: usize, rows: usize, r: u8, g: u8, b: u8) {
        self.ctx.draw_grid(cols, rows, Some(Color::TrueColor { r, g, b }));
    }

    fn draw_axes(&mut self, x_min: f64, x_max: f64, y_min: f64, y_max: f64) {
        // Guardamos los rangos internamente para normalize_coords
        self.ctx.set_ranges((x_min, x_max), (y_min, y_max));
        // Dibujamos visualmente
        self.ctx.draw_axes((x_min, x_max), (y_min, y_max), Some(Color::White));
    }

    fn draw_text(&mut self, text: &str, x: f64, y: f64, color_name: Option<&str>) {
        let color = parse_color(color_name);
        self.ctx.text(text, x, y, color);
    }
    
    /// Recibe una lista de tuplas de Python [(x, y), (x, y)...]
    fn scatter(&mut self, points: Vec<(f64, f64)>, color_name: Option<&str>) {
        let color = parse_color(color_name);
        self.ctx.scatter(&points, color);
    }

    fn line_chart(&mut self, points: Vec<(f64, f64)>, color_name: Option<&str>) {
        let color = parse_color(color_name);
        self.ctx.line_chart(&points, color);
    }

    fn render(&self) -> String {
        self.ctx.canvas.render()
    }

    fn clear(&mut self) {
        self.ctx.canvas.clear();
    }
}

// Función auxiliar para convertir strings de Python ("red", "blue") a colores de Rust
fn parse_color(name: Option<&str>) -> Option<Color> {
    match name {
        Some("red") => Some(Color::Red),
        Some("green") => Some(Color::Green),
        Some("blue") => Some(Color::Blue),
        Some("yellow") => Some(Color::Yellow),
        Some("cyan") => Some(Color::Cyan),
        _ => None,
    }
}

#[pymodule]
fn termplotpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Plotter>()?;
    Ok(())
}
