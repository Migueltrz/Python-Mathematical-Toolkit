# Mathematical Toolkit

This project is a **modular mathematical toolkit** built in **Python**, designed to perform operations ranging from basic arithmetic to symbolic optimization, statistical analysis, and graphical visualization.  
The main entry point is `calculadora.py`, which integrates multiple modules for extended functionality:  
`basico.py`, `estadistica.py`, `optimizar.py`, and `avanzado.py`.

---

## Table of Contents

<details>
  <summary>Click to expand</summary>

1. [Theoretical Framework](#theoretical-framework)
2. [Methodology and Code Structure](#methodology-and-code-structure)
3. [Results](#results)
4. [Conclusions](#conclusions)
5. [Installation](#installation)
6. [Execution](#execution)
7. [Contributing](#contributing)
8. [License](#license)

</details>

---

## Theoretical Framework

| Concept | Description |
|----------|-------------|
| **Arithmetic Operations** | Foundation of all mathematical computation; addition, subtraction, multiplication, and division form the base for higher-level functions. |
| **Statistical Analysis** | Involves summarizing, filtering, and visualizing datasets to extract insights through descriptive statistics and histograms. |
| **Symbolic Optimization** | Uses symbolic differentiation to locate critical points and determine minima or maxima of mathematical functions. |
| **Calculus and Graphing** | Graphical and symbolic approaches to functions using integration, derivatives, and visualization techniques. |

This toolkit combines **symbolic mathematics**, **numerical computation**, and **data visualization** using libraries such as **Sympy**, **Numpy**, **Pandas**, and **Matplotlib**.

---

## Methodology and Code Structure

The system is structured around modular programming principles, where each Python file encapsulates a specific set of mathematical capabilities.  
The central control and user interaction occur through `calculadora.py`.

```
📦 Math-Toolkit
 ┣ 📜 README.md
 ┣ 📜 calculadora.py
 ┣ 📜 basico.py
 ┣ 📜 estadistica.py
 ┣ 📜 optimizar.py
 ┣ 📜 avanzado.py
 ┗ 📂 data/
```

---

### `calculadora.py` — Main Program

Acts as the **main control module**, integrating all mathematical functionalities.  
It manages **user input**, executes **menu navigation**, and calls methods from the other modules.  
This file serves as the command-line interface where users can select between arithmetic, statistical, optimization, or advanced modes.

* **Core Tasks:**
  - Handles the main loop and user interaction.
  - Imports and executes functions from other modules dynamically.
  - Validates user input to prevent runtime errors.

Example structure:
```python
from basico import *
from estadistica import *
from optimizar import *
from avanzado import *

# Example of main control structure
option = input("Select mode: Basic (b), Statistics (s), Optimization (o), Advanced (a): ")
if option == 'b':
    basico.func_b()
elif option == 's':
    estadistica.func_e()
elif option == 'o':
    optimizar.opt()
elif option == 'a':
    avanzado.func_a()
```

---

### `basico.py` — Basic Mathematical Operations

Implements **elementary arithmetic functions** such as addition, subtraction, multiplication, and division, as well as power, root, and logarithmic operations.  
It serves as the foundation of the toolkit.

* **Features:**
  - Input validation to ensure numerical data.
  - Handles errors gracefully (e.g., division by zero).
  - Organized via simple function definitions.

---

### `estadistica.py` — Descriptive Statistics and Histograms

Provides methods for **exploratory data analysis** on CSV files using Pandas and Matplotlib.

* **`filt()`**:  
  - Reads a CSV file and generates **descriptive statistics** using `DataFrame.describe()`.
  - Allows the user to select specific statistics (mean, std, min, max) to export to a new CSV.

* **`hist()`**:  
  - Generates histograms for a selected column in a dataset.
  - Includes multiple filtering modes: numerical range, year extraction, text matching, or full-column plotting.

Example:
```python
plt.hist(d_hist, bins=10, alpha=0.5)
plt.xlabel(c_hist)
plt.ylabel('Frequency')
plt.title(f'Histogram of {c_hist}')
plt.show()
```

---

### `optimizar.py` — Symbolic Optimization

Performs **symbolic differentiation** to identify and classify **critical points** of a function using `Sympy`.

* **Process:**
  1. Receives a user-defined function \( f(x) \).
  2. Computes the first and second derivatives.
  3. Solves \( f'(x) = 0 \) for critical points.
  4. Evaluates \( f''(x) \) to classify maxima, minima, or inflection points.

Example:
```python
x = sp.Symbol("x")
fun = sp.sympify("x**3 - 3*x + 1")
d_1 = sp.diff(fun, x)
d_2 = sp.diff(d_1, x)
pcr = sp.solve(d_1, x)
```

---

### `avanzado.py` — Graphing and Integration

Contains methods for **function plotting** and **integration**.

* **`graf()`**:
  - Uses Numpy and Matplotlib to graph mathematical expressions within a user-defined range.
  - Accepts functions such as `np.sin(x)`, `np.exp(x)`, or any valid Numpy expression.

* **`inte()`**:
  - Computes both **definite** and **indefinite** integrals symbolically using Sympy.
  - Prompts the user for the limits of integration or performs indefinite integration when requested.

Example:
```python
x = sp.Symbol('x')
f = sp.sympify('x**2 + 3*x')
integral = sp.integrate(f, (x, 0, 2))
```

---

## Results

This toolkit provides users with a **multi-functional environment** for performing:
* Arithmetic operations  
* Statistical data exploration  
* Symbolic optimization  
* Function visualization and integration  

The application successfully integrates symbolic computation with numerical and graphical techniques to support **learning and analysis in mathematics, physics, and engineering contexts**.

---

## Conclusions

The **Mathematical Toolkit** demonstrates the power of modular programming in Python by combining **symbolic**, **numerical**, and **graphical** computation.  
Its structure makes it easy to extend with new features such as differential equations or regression analysis.

This system serves as both an **educational tool** and a **practical reference** for developing mathematical software using Python.

---

## Installation

### Requirements
- Python ≥ 3.8  
- Libraries:  
  `sympy`, `numpy`, `matplotlib`, `pandas`, `seaborn`

### Installation Command
```bash
pip install sympy numpy matplotlib pandas seaborn
```

---

## Execution

Run the program from the terminal using:
```bash
python calculadora.py
```

Ensure all modules (`basico.py`, `estadistica.py`, `optimizar.py`, `avanzado.py`) are in the same directory as `calculadora.py`.

---

## Contributing

Contributions, feedback, and suggestions are welcome.  
You may open a **Pull Request** or report issues in the **Issues** section.

---

## License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.
