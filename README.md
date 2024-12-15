# DataViz

Got it! Here's the updated **README.md** content with the **Motivation** seamlessly integrated into the introduction of `DataViz`.

---

# **DataViz**

**DataViz** is a Python module designed to help users visualize data structures and operations using symbolic representations and `matplotlib`. It supports visualizing lists, strings, and arithmetic operations in an interactive and intuitive way.  

---

## **Motivation**

Data Science is one of the pillars of today’s scientific development and education. It aims to identify similarities in patterns for prediction and classification. Therefore, teaching data science algorithms and methods relies heavily on intuition and visualization.

The inspiration for this module comes from the teaching methods of **Nicholas Saunderson (1682–1739)**, a blind professor of mathematics at Cambridge University who developed palpable arithmetic, a tactile method for identifying numbers and shapes through touch. Saunderson’s ideas, which predate the Braille system, emphasized intuitive learning and simple distinctions to convey concepts.

The **DataViz** module aims to extend this philosophy to the teaching of **Python** and **Data Science**, especially for students with learning impairments. By presenting fundamental concepts and stressing similarities and patterns through visualizations, this module creates an easy-to-understand and intuitive learning experience for all learners.

---

## **Features**

- **Visualize Lists**: Display lists with symbolic representations.
- **String Visualization**: Represent strings as groups of dots for analysis and modification.
- **Symbolic Arithmetic**: Perform operations on numbers and view results symbolically.
- **Interactive Modifications**: Append, insert, remove, slice, and replace elements with visual feedback.

---

## **Installation**

To use this module, you need Python installed on your machine.

### **Step 1: Clone the Repository**

Clone this repository from GitHub:

```bash
git clone https://github.com/urja-hub/DataViz.git
```

### **Step 2: Install Dependencies**

Navigate to the project folder and install required dependencies using `pip`:

```bash
cd DataViz
pip install matplotlib
```

---

## **How to Use**

1. Place the `DataViz` module in your Python project directory.
2. Import the module components into your script.

### **Example 1: Visualizing Lists**
```python
from dataviz.lists import ListSymbolPlotter

# Create an instance of the ListSymbolPlotter
plotter = ListSymbolPlotter()

# Visualize a list
sample_list = [1, 2.5, True, 'A', 3+4j]
plotter.plot_list(sample_list)
```

### **Example 2: Visualizing Strings**
```python
from dataviz.String import StringDotPlotter

# Create an instance of StringDotPlotter
string_plotter = StringDotPlotter(group_size=2)

# Visualize string
sample_string = "DataViz"
string_plotter.plot_string(sample_string)
```

### **Example 3: Performing Operations**
```python
from dataviz.Operations import perform_operation

# Run an interactive arithmetic operation
perform_operation()
```

### **Example 4: Customizing Plot Frame Size**
```python
from dataviz.utils import set_frame_size

# Adjust the frame size for plots
set_frame_size(8, 6)
```

---

## **Project Structure**

```bash
DataViz/
│
├── __init__.py       # Module initialization
├── lists.py          # List visualization
├── String.py         # String visualization
├── Operations.py     # Arithmetic operations
├── symbols.py        # Symbol mappings
├── utils.py          # Utility functions (e.g., set frame size)
└── README.md         # Project documentation
```

---

## **License**

This project is licensed under the MIT License.

---

## **Contributing**

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and submit a pull request.

---

Let me know if this works or if you'd like further refinements! 🚀
