import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

# Define XOR-based encryption for testing CA-based fractal decryption

def xor_encrypt(data, key):
    """Simple XOR encryption of a binary image."""
    return np.bitwise_xor(data, key)

def xor_decrypt(data, key):
    """XOR decryption is the same as encryption."""
    return np.bitwise_xor(data, key)

# Define CA-based fractal decryption applied to XOR-encrypted data

def apply_fractal_decrypt(grid, depth):
    """Apply a Menger sponge-inspired decryption process."""
    size = grid.shape[0]
    new_grid = np.copy(grid)
    
    kernel_3x3x3 = np.ones((3, 3))
    kernel_3x3x3[1, :] = 0
    kernel_3x3x3[:, 1] = 0
    
    for _ in range(depth):
        neighbor_count = convolve(grid, kernel_3x3x3, mode='constant', cval=0)
        new_grid = (neighbor_count >= 4) & grid
    
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

# Generate a simple binary fractal image for testing
original_image = np.random.choice([0, 1], size=(grid_size, grid_size))
key = np.random.choice([0, 1], size=(grid_size, grid_size))  # Random XOR key

# Encrypt with XOR
encrypted_image = xor_encrypt(original_image, key)

decrypted_fractal = apply_fractal_decrypt(encrypted_image, ca_depth)

# Visualize results
visualize_image(original_image, "Original Binary Image")
visualize_image(encrypted_image, "XOR Encrypted Image")
visualize_image(decrypted_fractal, "Fractal-Based Decryption Attempt")