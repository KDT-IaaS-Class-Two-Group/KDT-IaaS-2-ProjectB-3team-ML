import os
import numpy as np
from PIL import Image
import torch

def preprocess_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img) / 255.0  # Normalize to 0-1
    img_tensor = torch.tensor(img_array, dtype=torch.float32).permute(2, 0, 1)
    return img_tensor