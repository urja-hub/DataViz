# symbols.py

import matplotlib.pyplot as plt

# Centralized symbol mapping
symbol_map = {
    True: "⬆",
    False: "⬇",
    int: "⬖",
    float: "⬙",
    complex: "◈",
    'char': "●",
    
}

class SymbolPlotter:
    def __init__(self):
        self.symbol_map = symbol_map

    def get_symbol(self, value):
        """Determine the symbol for the given value and plot it."""
        symbol = self.get_symbol_string(value)
        if symbol is not None:
            self.plot_symbol(symbol)
        else:
            print('Not a supported datatype')

    def get_symbol_string(self, value):
        """Determine the symbol for the given value (returns symbol as a string)."""
        if isinstance(value, bool):
            return self.symbol_map[value]
        elif isinstance(value, (int, float, complex)):
            return self.symbol_map[type(value)]
        elif isinstance(value, str) and len(value) == 1:
            return self.symbol_map['char']
        else:
            return None
        
    def plot_symbol(self, datatype):
        import matplotlib.pyplot as plt
        figsize = plt.rcParams.get('figure.figsize', (6, 4))  # Fetch the current figure size
        print(f"Using figure size: {figsize}")  # Debugging print to ensure size is fetched
        plt.figure(figsize=figsize)
        plt.text(0.5, 0.5, datatype, fontsize=50, ha='center', va='center', wrap=True)
        plt.axis('off')
        plt.show()





# example

#symbol_plotter = SymbolPlotter()
#symbol_plotter.get_symbol(True)