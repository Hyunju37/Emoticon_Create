import time
import keras_cv
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import numpy  as np

keras.mixed_precision.set_global_policy("mixed_float16")
model = keras_cv.models.StableDiffusion(jit_compile=True)
#이미지 저장
def save_images(images):
    save_dir = "generated_images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, image in enumerate(images, start=1):
        filename = f"image_{i}.jpg"
        file_path = os.path.join(save_dir, filename)
        
        if len(image.shape) == 4:
            image = np.squeeze(image)
        
        pil_image = Image.fromarray(image)
        pil_image.save(file_path, format='JPEG', quality=75)
        
#이미지 시각화
def plot_images(images):
    
    plt.figure(figsize=(6.5, 6.5))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
    plt.show()


