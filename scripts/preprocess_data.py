import os
import numpy as np
from PIL import Image
import torch
from .preprocess.preprocess_image import preprocess_image

def preprocess_and_save_data(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            img_tensor = preprocess_image(os.path.join(input_dir, filename))
            torch.save(img_tensor, os.path.join(output_dir, filename.replace('.png', '.pt')))

if __name__ == "__main__":
    preprocess_and_save_data('data/train_data', 'data/preprocess_data')
