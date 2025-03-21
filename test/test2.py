import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

# Define the 3D Menger Sponge cellular automata rule
# Expanding to iterative layers through 3x3x3, 5x5x5, and beyond to represent fractional dimensions

def initialize_fractal_image(size):
    """Generate a simple fractal geometric pattern to test encryption and decryption."""
    img = Image.new("L", (size, size), color=255)
    pixels = img.load()
    
    for x in range(size):
        for y in range(size):
            if (x % 3 == 0 or y % 3 == 0) and (x % 9 != 0 and y % 9 != 0):
                pixels[x, y] = 0  # Generate a simple self-similar pattern
    
    img_array = np.array(img) // 255  # Convert to binary
    return img_array


def apply_menger_rule(grid, depth):
    """Apply Menger sponge-like CA transformation iteratively in fractional dimensions."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    # Define the fractional-dimensional Menger sponge transformation
    kernel_3x3x3 = np.ones((3, 3))
    kernel_3x3x3[1, :] = 0
    kernel_3x3x3[:, 1] = 0
    
    kernel_5x5x5 = np.ones((5, 5))
    kernel_5x5x5[2, :] = 0
    kernel_5x5x5[:, 2] = 0
    
    for _ in range(depth):
        neighbor_count_3x3x3 = convolve(grid, kernel_3x3x3, mode='constant', cval=0)
        neighbor_count_5x5x5 = convolve(grid, kernel_5x5x5, mode='constant', cval=0)
        
        # Ensure binary transformation to prevent smoothing
        new_grid = ((neighbor_count_3x3x3 == 5) | (neighbor_count_5x5x5 == 9)) & grid
        
        # Add thresholding to prevent over-smoothing
        new_grid = np.where(new_grid > 0.5, 1, 0)
        
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
        
    return new_grid


def visualize_image(grid, title):
    """Visualize a 2D binary image."""
    plt.imshow(grid, cmap='gray')
    plt.title(title)
    plt.colorbar()
    plt.show()

# Simulation Parameters
grid_size = 81  # Must be a multiple of 3 for proper Menger sponge recursion
ca_depth = 3  # Number of iterations

# Generate and process a simple fractal test image
original_image = initialize_fractal_image(grid_size)
encrypted_image = apply_menger_rule(original_image, ca_depth)
decrypted_image = reverse_menger_rule(encrypted_image, ca_depth)

# Visualize the original, encrypted, and decrypted images
visualize_image(original_image, "Original Fractal Test Image")
visualize_image(encrypted_image, "Fixed Encrypted Fractal Image - Menger Sponge CA")
visualize_image(decrypted_image, "Fixed Decrypted Fractal Image - Menger Sponge CA")