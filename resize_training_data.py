import os
from PIL import Image


path = "./resources/unprocessed_training_data/pokemon_to_resize/"
save_path = "./resources/training_data/resized/"
size = 56, 56

for filename in os.listdir(path):
    outfile = os.path.splitext(filename)[0] + ".resized.png"
    try:
        im = Image.open(os.path.join(path, filename))
        width, height = im.size
        w_factor = 56 / width
        h_factor = 56 / height
        im = im.resize((int(w_factor * width), int(h_factor * height)), Image.ANTIALIAS)
        im.save(os.path.join(save_path, outfile))
    except IOError:
        print("cannot create thumbnail for '%s'" % filename)
