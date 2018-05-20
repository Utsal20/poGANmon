import os
from PIL import Image

path = "./resources/training_data/"

for filename in os.listdir(path):
    im = Image.open(os.path.join(path, filename))
    width, height = im.size
    if (width, height) != (56, 56):
        w_ratio = 56 / width
        h_ratio = 56 / height
        im = im.resize((int(width * w_ratio), int(height * h_ratio)))
        im.save(os.path.join(path, filename))
