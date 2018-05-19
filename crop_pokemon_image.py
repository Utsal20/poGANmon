from PIL import Image
import os.path


def crop(path, image_file, height, width):
    k = 1
    imgwidth, imgheight = image_file.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j+width, i+height)
            o = image_file.crop(box)
            o.save(os.path.join(path, "%s.png" % k))
            k += 1


if __name__ == '__main__':
    imageToPartition = Image.open("./resources/unprocessed_training_data/training_examples_uncropped.png")
    crop("./resources/training_data/", imageToPartition, 56, 56)
