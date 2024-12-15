import matplotlib.pyplot as plt

def set_frame_size(width, height):
    """Adjust the frame size for plots."""
    plt.rcParams['figure.figsize'] = (width, height)
