from PIL import Image
import os

def rgb_to_grayscale(input_dir, output_dir):
    if not os.path.exists(output_dir):  # cria diretorio destino
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            with Image.open(os.path.join(input_dir, filename)) as img:
                grayscale_img = img.convert('L')
                grayscale_img.save(os.path.join(output_dir, filename))

input_directory = "rgb_images"
output_directory = "gray_images"
rgb_to_grayscale(input_directory, output_directory)
