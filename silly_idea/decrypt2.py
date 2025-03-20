import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Define the 3D Menger Sponge cellular automata rule
# Expanding to iterative layers through 3x3x3, 5x5x5, and beyond to represent 4D structures

def initialize_grid(size):
    """Initialize a 4D grid with a random binary distribution."""
    return np.random.choice([0, 1], size=(size, size, size, size), p=[0.5, 0.5])


def apply_menger_rule(grid, depth):
    """Apply Menger sponge-like CA transformation iteratively in 4D."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    # Define the 4D kernel for the Menger sponge
    kernel_3x3x3 = np.ones((3, 3, 3))
    kernel_3x3x3[1, 1, :] = 0
    kernel_3x3x3[1, :, 1] = 0
    kernel_3x3x3[:, 1, 1] = 0
    
    kernel_5x5x5 = np.ones((5, 5, 5))
    kernel_5x5x5[2, :, :] = 0
    kernel_5x5x5[:, 2, :] = 0
    kernel_5x5x5[:, :, 2] = 0
    
    kernel_4D = np.ones((3, 3, 3, 3))
    kernel_4D[1, 1, :, :] = 0
    kernel_4D[1, :, 1, :] = 0
    kernel_4D[:, 1, 1, :] = 0
    kernel_4D[:, :, 1, 1] = 0
    
    for _ in range(depth):
        neighbor_count_3x3x3 = convolve(grid, kernel_3x3x3[..., None], mode='constant', cval=0)
        neighbor_count_5x5x5 = convolve(grid, kernel_5x5x5[..., None], mode='constant', cval=0)
        neighbor_count_4D = convolve(grid, kernel_4D, mode='constant', cval=0)
        
        # Apply transformation: Menger sponge-like rule expands recursively
        new_grid = ((neighbor_count_3x3x3 == 13) | (neighbor_count_3x3x3 == 5) | 
                    (neighbor_count_5x5x5 == 21) | (neighbor_count_5x5x5 == 9) | 
                    (neighbor_count_4D == 17) | (neighbor_count_4D == 7)) & grid
        grid = np.copy(new_grid)
    
    return new_grid


def visualize_slice(grid, z_slice, w_slice):
    """Visualize a 2D slice of the 4D structure."""
    plt.imshow(grid[:, :, z_slice, w_slice], cmap='gray')
    plt.title(f"Menger Sponge 4D CA - Slices z={z_slice}, w={w_slice}")
    plt.colorbar()
    plt.show()

# Simulation Parameters
grid_size = 27  # Must be a power of 3 for proper Menger sponge recursion
ca_depth = 3  # Number of iterations

grid = initialize_grid(grid_size)
transformed_grid = apply_menger_rule(grid, ca_depth)

# Visualize a slice
visualize_slice(transformed_grid, z_slice=grid_size//2, w_slice=grid_size//2)
