import os

path = "./resources/file_renaming/"

for filename in os.listdir(path):
    newName = int(filename[0:3]) - 32
    newName = str(newName) + '.png'
    os.rename(os.path.join(path, filename), os.path.join(path, newName))
