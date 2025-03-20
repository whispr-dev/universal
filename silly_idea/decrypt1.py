import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Define the 3D Menger Sponge cellular automata rule
# Rule: Cells activate based on a recursive Menger sponge-like structure

def initialize_grid(size):
    """Initialize a 3D grid with a random binary distribution."""
    return np.random.choice([0, 1], size=(size, size, size), p=[0.5, 0.5])


def apply_menger_rule(grid, depth):
    """Apply Menger sponge-like CA transformation iteratively."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    # Define the 3D kernel for the Menger sponge
    kernel = np.ones((3, 3, 3))
    kernel[1, 1, :] = 0
    kernel[1, :, 1] = 0
    kernel[:, 1, 1] = 0
    
    for _ in range(depth):
        neighbor_count = convolve(grid, kernel, mode='constant', cval=0)
        
        # Apply transformation: Only keep active cells if they match the Menger sponge recursion
        new_grid = ((neighbor_count == 13) | (neighbor_count == 5)) & grid  # Example condition
        grid = np.copy(new_grid)
    
    return new_grid


def visualize_slice(grid, z_slice):
    """Visualize a 2D slice of the 3D structure."""
    plt.imshow(grid[:, :, z_slice], cmap='gray')
    plt.title(f"Menger Sponge 3D CA - Slice {z_slice}")
    plt.colorbar()
    plt.show()

# Simulation Parameters
grid_size = 27  # Must be a power of 3 for proper Menger sponge recursion
ca_depth = 3  # Number of iterations

grid = initialize_grid(grid_size)
transformed_grid = apply_menger_rule(grid, ca_depth)

# Visualize a slice
visualize_slice(transformed_grid, z_slice=grid_size//2)
