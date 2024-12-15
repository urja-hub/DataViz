from .symbols import SymbolPlotter
import matplotlib.pyplot as plt
from .utils import set_frame_size

class ListSymbolPlotter:
    def __init__(self):
        self.symbol_plotter = SymbolPlotter()

    def __call__(self, lst):
        """Make the object callable to plot the list."""
        self.plot_list(lst)

    def plot_list(self, lst):
        """Plot the symbolic representation of a list."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        print("Current figure size:", plt.rcParams['figure.figsize'])  # Debug

        symbols = []
        for item in lst:
            symbol = self.symbol_plotter.get_symbol_string(item)
            symbols.append(symbol if symbol is not None else "?")

        symbolic_representation = f"[ {', '.join(symbols)} ]"

        plt.figure(figsize=plt.rcParams['figure.figsize'])
        plt.text(
            0.5,
            0.5,
            symbolic_representation,
            ha="center",
            va="center",
            wrap=True,
            fontsize=50,
        )
        plt.axis("off")
        plt.show()


def pop_and_plot(self, lst, index=-1):
    """Remove an element at the given index and plot the updated list.
    
    Args:
        lst (list): The list to modify.
        index (int): The index of the element to remove. Defaults to -1 (last element).

    Raises:
        TypeError: If the input is not a list.
        IndexError: If the index is out of bounds.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    if not (-len(lst) <= index < len(lst)):
        raise IndexError(f"Index {index} is out of bounds for the list.")
    
    print("Before popping:")
    self.plot_list(lst)

    popped_item = lst.pop(index)
    print(f"Popped element: {popped_item}")

    print("After popping:")
    self.plot_list(lst)


    def access_and_plot(self, lst, index):
        """Access an element at the given index and plot its symbolic representation."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        if not 0 <= index < len(lst):
            print(f"Error: Index {index} is out of bounds for the list.")
            return

        element = lst[index]
        symbol = self.symbol_plotter.get_symbol_string(element) or "?"

        plt.figure()
        plt.text(
            0.5, 0.5,
            f"Element at index {index}: {symbol}",
            ha="center", va="center", wrap=True, fontsize=30
        )
        plt.axis("off")
        plt.show()

    def slice_and_plot(self, lst, start=None, end=None):
        """Slice a list and plot the symbolic representation of the sliced portion."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        sliced_list = lst[start:end]
        print(f"Sliced List: {sliced_list}")

        symbols = [
            self.symbol_plotter.get_symbol_string(item) or "?"
            for item in sliced_list
        ]

        symbolic_representation = f"[ {', '.join(symbols)} ]"

        plt.figure()
        plt.text(
            0.5, 0.5,
            symbolic_representation,
            ha="center", va="center", wrap=True, fontsize=50
        )
        plt.axis("off")
        plt.show()

    def calculate_length(self, lst):
        """Calculate and display the length of the list."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        length = len(lst)
        print(f"Length of the list: {length}")

        plt.figure()
        plt.text(
            0.5, 0.5,
            f"Length of list: {length}",
            ha="center", va="center", wrap=True, fontsize=30
        )
        plt.axis("off")
        plt.show()
        return length

    def append_and_plot(self, lst, element):
        """Append an element to the list and plot the updated list."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        lst.append(element)
        print(f"After appending: {lst}")
        self.plot_list(lst)

    def insert_and_plot(self, lst, index, element):
        """Insert an element at a specific index and plot the updated list."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        if not 0 <= index <= len(lst):
            print(f"Error: Index {index} is out of bounds.")
            return

        lst.insert(index, element)
        print(f"After inserting: {lst}")
        self.plot_list(lst)

    def find_and_plot(self, lst, element):
        """Find an element in the list and visualize its index."""
        if not isinstance(lst, list):
            print("Error: Input is not a list.")
            return

        try:
            index = lst.index(element)
            print(f"Element '{element}' found at index: {index}")
            self.access_and_plot(lst, index)
        except ValueError:
            print(f"Element '{element}' not found in the list.")
