import os
import sys
import matplotlib.pyplot as plt

# Adjust imports to handle standalone and package modes
if __name__ == "__main__":
    # Running as a standalone script
    from symbols import SymbolPlotter
else:
    # Running as part of a package
    from .symbols import SymbolPlotter

# Add the current file's directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def perform_operation():
    print("Hellos yoooo")
    try:
        num1 = input("Enter the first number (can be int, float, or complex): ").strip()
        num1 = parse_input(num1)
        operator = input("Enter an operator (+, -, *, /, %, //, **): ").strip()
        if operator not in ["+", "-", "*", "/", "%", "//", "**"]:
            print("Invalid operator. Please enter one of +, -, *, /, %, //, **.")
            return
        num2 = input("Enter the second number (can be int, float, or complex): ").strip()
        num2 = parse_input(num2)
        if operator in ["/", "//"] and isinstance(num2, (int, float)) and num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "%":
            result = num1 % num2
        elif operator == "//":
            result = num1 // num2
        elif operator == "**":
            result = num1 ** num2

        symbol_plotter = SymbolPlotter()
        symbol1 = symbol_plotter.get_symbol_string(num1)
        symbol2 = symbol_plotter.get_symbol_string(num2)
        symbol_result = symbol_plotter.get_symbol_string(result)

        display_equation(num1, operator, num2, result, symbol1, symbol2, symbol_result)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def parse_input(value):
    try:
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
        elif "." in value and "j" not in value:
            float_value = float(value)
            if float_value.is_integer():
                return int(float_value)
            return float_value
        elif "j" in value:
            return complex(value)
        else:
            raise ValueError("Invalid number format.")
    except ValueError:
        print("Error: Please enter a valid number (int, float, or complex).")
        raise

def display_equation(num1, operator, num2, result, symbol1, symbol2, symbol_result):
    plt.figure(figsize=(6, 1.5))
    plt.axis("off")
    equation_text = f"{num1} {operator} {num2} ="
    result_text = f"{result}"
    symbolic_text = f"{symbol1} {operator} {symbol2} ="
    symbolic_result_text = f"{symbol_result}"
    result_x_position = len(equation_text) * 0.041
    plt.text(0.1, 0.7, equation_text, fontsize=15, ha="left", va="center")
    plt.text(result_x_position, 0.7, result_text, fontsize=15, ha="left", va="center", color="red")
    plt.text(0.1, 0.4, symbolic_text, fontsize=15, ha="left", va="center")
    plt.text(result_x_position, 0.4, symbolic_result_text, fontsize=15, ha="left", va="center", color="red")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
    plt.show()

if __name__ == "__main__":
    perform_operation()
