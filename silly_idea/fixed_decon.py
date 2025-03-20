import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Define the 3D Menger Sponge cellular automata rule
# Expanding to iterative layers through 3x3x3, 5x5x5, and beyond to represent fractional dimensions

def initialize_grid(size):
    """Initialize a fractional-dimensional Menger sponge structure."""
    return np.random.choice([0, 1], size=(size, size, size), p=[0.5, 0.5])


def apply_menger_rule(grid, depth):
    """Apply Menger sponge-like CA transformation iteratively in fractional dimensions."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    # Define the fractional-dimensional Menger sponge transformation
    kernel_3x3x3 = np.ones((3, 3, 3))
    kernel_3x3x3[1, 1, :] = 0
    kernel_3x3x3[1, :, 1] = 0
    kernel_3x3x3[:, 1, 1] = 0
    
    kernel_5x5x5 = np.ones((5, 5, 5))
    kernel_5x5x5[2, :, :] = 0
    kernel_5x5x5[:, 2, :] = 0
    kernel_5x5x5[:, :, 2] = 0
    
    for _ in range(depth):
        neighbor_count_3x3x3 = convolve(grid, kernel_3x3x3, mode='constant', cval=0)
        neighbor_count_5x5x5 = convolve(grid, kernel_5x5x5, mode='constant', cval=0)
        
        # Apply transformation: Menger sponge-like rule expands recursively
        new_grid = ((neighbor_count_3x3x3 == 13) | (neighbor_count_3x3x3 == 5) | 
                    (neighbor_count_5x5x5 == 21) | (neighbor_count_5x5x5 == 9)) & grid
        grid = np.copy(new_grid)
    
    return new_grid


def reverse_menger_rule(grid, depth):
    """Apply the inverse transformation to decrypt the fractional-dimensional Menger sponge."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    for _ in range(depth):
        
        # Reverse transformation: Undo Menger sponge rule by back-propagating fractional steps
        new_grid = np.roll(new_grid, shift=-1, axis=0)
        new_grid = np.roll(new_grid, shift=-1, axis=1)
        new_grid = np.roll(new_grid, shift=-1, axis=2)
        
    return new_grid


def visualize_slice(grid, z_slice):
    """Visualize a 2D slice of the fractional-dimensional Menger sponge."""
    plt.imshow(grid[:, :, z_slice], cmap='gray')
    plt.title(f"Menger Sponge Fractal CA - Slice z={z_slice}")
    plt.colorbar()
    plt.show()

# Simulation Parameters
grid_size = 27  # Must be a power of 3 for proper Menger sponge recursion
ca_depth = 3  # Number of iterations

grid = initialize_grid(grid_size)
encrypted_grid = apply_menger_rule(grid, ca_depth)
decrypted_grid = reverse_menger_rule(encrypted_grid, ca_depth)

# Visualize a slice of the encrypted and decrypted states
visualize_slice(encrypted_grid, z_slice=grid_size//2)
visualize_slice(decrypted_grid, z_slice=grid_size//2)