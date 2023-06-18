import time
import keras_cv
import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image

#keras.mixed_precision.set_global_policy("mixed_float16")
#model = keras_cv.models.StableDiffusion(jit_compile=True)

def save_images(images):
    save_dir="generated_images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i,image in enumerate(images):
        filename = f"image_{i}.jpg"
        file_path=os.path.join(save_dir,filename)
        pil_image = Image.fromarray(image)
        pil_image.save(file_path, format='JPEG', quality=75)

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
    plt.show()
# 주어진 텍스트로 이미지를 생성합니다.
#gen_image = model.text_to_image(
#    "happiness people",
#   batch_size=1,
#)
#plot_images(gen_image)
#save_images(gen_image)
