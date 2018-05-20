import os
from PIL import Image

path = "./resources/training_data/resized"

for filename in os.listdir(path):
    image = Image.open(os.path.join(path, filename)).convert('RGBA')
    background = Image.new('RGBA', image.size, (255, 255, 255))

    alpha_composite = Image.alpha_composite(background, image)
    alpha_composite.save(os.path.join(path, filename))
