import matplotlib.pyplot as plt

class StringDotPlotter:
    def __init__(self, group_size=1):
        """
        Initialize the StringDotPlotter with a customizable group size.
        Args:
            group_size (int): Number of letters each dot represents.
        """
        if group_size < 1:
            raise ValueError("Group size must be at least 1.")
        self.group_size = group_size

    def __call__(self, string):
        """Make the object callable to plot the string."""
        self.plot_string(string)

    def plot_string(self, string, highlights=None, title=""):
        """
        Plot the string as groups of dots.
        Args:
            string (str): Input string to be visualized.
            highlights (list): Indices of groups to highlight in red.
            title (str): Title for the plot.
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string.")

        groups = self._string_to_groups(string)
        dots = ["●" for _ in groups]

        # Highlight specific groups
        if highlights:
            for i in highlights:
                if 0 <= i < len(dots):
                    dots[i] = "●"  # Red dot for highlights

        # Plot the dots
        plt.figure(figsize=(8, 2))
        for i, dot in enumerate(dots):
            color = "red" if i in (highlights or []) else "black"
            plt.text(
                0.5 + i * 0.1,
                0.5,
                dot,
                ha="center",
                va="center",
                fontsize=30,
                family="monospace",
                color=color,
            )
        plt.axis("off")
        plt.title(title)
        plt.show()

    def _string_to_groups(self, string):
        """Split string into groups based on group size."""
        return [string[i:i + self.group_size] for i in range(0, len(string), self.group_size)]

    def append_and_plot(self, string, char):
        """Append a character to the string and visualize the update."""
        before = string
        after = string + char
        print(f"Before: {before}")
        print(f"After: {after}")

        groups = self._string_to_groups(after)
        highlights = [len(groups) - 1]  # Highlight the last group

        self.plot_string(before, title="Before Append")
        self.plot_string(after, highlights=highlights, title="After Append")

        return after

    def insert_and_plot(self, string, index, char):
        """Insert a character at a specific index and visualize the update."""
        before = string
        after = string[:index] + char + string[index:]
        print(f"Before: {before}")
        print(f"After: {after}")

        groups = self._string_to_groups(after)
        highlight_group = index // self.group_size  # Determine the group of the insertion point

        self.plot_string(before, title="Before Insert")
        self.plot_string(after, highlights=[highlight_group], title="After Insert")

        return after

    def pop_and_plot(self, string, index=-1):
        """Remove a character at the given index and visualize the update."""
        before = string
        popped_char = string[index]
        after = string[:index] + string[index + 1:]
        print(f"Before: {before}")
        print(f"Popped character: {popped_char}")
        print(f"After: {after}")

        groups = self._string_to_groups(before)
        highlight_group = (index % len(string)) // self.group_size  # Determine the group of the removed character

        self.plot_string(before, highlights=[highlight_group], title="Before Pop")
        self.plot_string(after, title="After Pop")

        return after

    def replace_and_plot(self, string, old_char, new_char):
        """Replace a character in the string with another and visualize the update."""
        if old_char not in string:
            print(f"Character '{old_char}' not found in the string.")
            return string

        before = string
        index = string.index(old_char)
        after = string.replace(old_char, new_char, 1)
        print(f"Before: {before}")
        print(f"After: {after}")

        groups = self._string_to_groups(after)
        highlight_group = index // self.group_size  # Determine the group of the replaced character

        self.plot_string(before, highlights=[highlight_group], title="Before Replace")
        self.plot_string(after, highlights=[highlight_group], title="After Replace")

        return after

    def slice_and_plot(self, string, start=None, end=None):
        """Slice a string and plot the updated dot representation."""
        before = string
        after = string[start:end]

        print(f"Before: {before}")
        print(f"Slicing indices: start={start}, end={end}")

        # Step View: Mark the sliced portion in red
        groups = self._string_to_groups(string)
        sliced_start = start // self.group_size if start is not None else 0
        sliced_end = -(-end // self.group_size) if end is not None else len(groups)

        # Plot Step Representation
        plt.figure(figsize=(8, 2))
        for i, group in enumerate(groups):
            color = "red" if sliced_start <= i < sliced_end else "black"
            plt.text(
                0.5 + i * 0.1,
                0.5,
                group,
                ha="center",
                va="center",
                fontsize=30,
                family="monospace",
                color=color,
            )
        plt.axis("off")
        plt.title("Step: Highlight Sliced Portion")
        plt.show()

        # Plot Final Sliced Representation
        self.plot_string(after, title="After Slice")
        return after


# Main program for user interaction
if __name__ == "__main__":
    string_dot_plotter = StringDotPlotter(group_size=2)
    test_string = input("Enter a string to visualize: ")

    while True:
        print("\nMenu:")
        print("1. Append a character")
        print("2. Insert a character")
        print("3. Pop a character")
        print("4. Replace a character")
        print("5. Slice the string")
        print("6. Exit")

        choice = input("Choose an operation: ")

        if choice == "1":
            char = input("Enter the character to append: ")
            test_string = string_dot_plotter.append_and_plot(test_string, char)
        elif choice == "2":
            index = int(input("Enter the index to insert at: "))
            char = input("Enter the character to insert: ")
            test_string = string_dot_plotter.insert_and_plot(test_string, index, char)
        elif choice == "3":
            index = int(input("Enter the index to pop (default: -1): ") or -1)
            test_string = string_dot_plotter.pop_and_plot(test_string, index)
        elif choice == "4":
            old_char = input("Enter the character to replace: ")
            new_char = input("Enter the new character: ")
            test_string = string_dot_plotter.replace_and_plot(test_string, old_char, new_char)
        elif choice == "5":
            start = input("Enter the start index (or press Enter for None): ")
            end = input("Enter the end index (or press Enter for None): ")
            start = int(start) if start else None
            end = int(end) if end else None
            test_string = string_dot_plotter.slice_and_plot(test_string, start, end)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
