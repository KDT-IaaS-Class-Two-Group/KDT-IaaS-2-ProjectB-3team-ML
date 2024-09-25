import numpy as np
from PIL import Image
import os

def generate_rgb_images(save_dir, size=(10, 10)):
    colors = {
        "R": [255, 0, 0],
        "G": [0, 255, 0],
        "B": [0, 0, 255]
    }
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for color_name, rgb in colors.items():
        img_array = np.full((size[0], size[1], 3), rgb, dtype=np.uint8)
        img = Image.fromarray(img_array)
        img.save(os.path.join(save_dir, f"{color_name}.png"))

if __name__ == "__main__":
    generate_rgb_images('data/test_data')
