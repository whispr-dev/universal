import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

# Define a 3.9D CA encryption method
def apply_3d_menger_encryption(grid, depth):
    """Apply a near-4D Menger sponge transformation for encryption."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    kernel_3x3x3 = np.ones((3, 3, 3))
    kernel_3x3x3[1, :, :] = 0
    kernel_3x3x3[:, 1, :] = 0
    kernel_3x3x3[:, :, 1] = 0
    
    for _ in range(depth):
        neighbor_count = convolve(grid, kernel_3x3x3, mode='constant', cval=0)
        new_grid = (neighbor_count >= 4) & grid
    
    return new_grid

# Define a 2D CA-based cryptanalysis method
def apply_2d_ca_cryptanalysis(grid, depth):
    """Apply a 2D CA-based cryptanalysis on a 3.9D encrypted dataset."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    kernel_3x3 = np.ones((3, 3))
    kernel_3x3[1, :] = 0
    kernel_3x3[:, 1] = 0
    
    for _ in range(depth):
        neighbor_count = convolve(grid[:, :, size // 2], kernel_3x3, mode='constant', cval=0)
        new_grid[:, :, size // 2] = (neighbor_count >= 3) & grid[:, :, size // 2]
    
    return new_grid[:, :, size // 2]


def visualize_image(grid, title):
    """Visualize a 2D binary image."""
    plt.imshow(grid, cmap='gray')
    plt.title(title)
    plt.colorbar()
    plt.show()

# Simulation Parameters
grid_size = 27  # Must be a power of 3 for Menger sponge recursion
ca_depth = 3  # Number of iterations

# Generate a structured fractal image for testing
def initialize_fractal_image(size):
    img = Image.new("L", (size, size), color=255)
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            if (x % 3 == 0 or y % 3 == 0) and (x % 9 != 0 and y % 9 != 0):
                pixels[x, y] = 0  # Generate a simple self-similar pattern
    img_array = np.array(img) // 255  # Convert to binary
    return img_array

original_image = initialize_fractal_image(grid_size)
original_3d = np.repeat(original_image[:, :, None], grid_size, axis=2)  # Extend to 3D for encryption

# Encrypt with near-4D Menger sponge transformation
encrypted_3d = apply_3d_menger_encryption(original_3d, ca_depth)

decrypted_2d = apply_2d_ca_cryptanalysis(encrypted_3d, ca_depth)

# Visualize results
visualize_image(original_image, "Original Fractal Image")
visualize_image(encrypted_3d[:, :, grid_size // 2], "3.9D Encrypted Image (Middle Slice)")
visualize_image(decrypted_2d, "2D Cryptanalysis Attempt on 3.9D Data")