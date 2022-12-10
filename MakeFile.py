# File used to create ImageInformation files from the command line.

import sys
import os
from PIL import Image # Must install pillow

# Makes sure the user inputted correct amount of information
if len(sys.argv) < 2:
    print("Input arguments as: image file, tile width, tile height, tile count or just image_file")
    raise 

image_name = "Images/" + sys.argv[1]

# Makes sure that the image file exists.
if not os.path.exists(image_name):
    print(f"{image_name} doesn't exist!")
    raise FileNotFoundError

file_name = sys.argv[1].removesuffix(".png")

# Removes the name of the image, but not the directory.
file_index = max(file_name.rfind("/"), file_name.rfind("\\"))
file_directory = ""
if file_index != -1:
    # Creates the directory if it doesn't exist.
    file_directory = file_name[:file_index]
    if not os.path.exists("ImageInformation/" + file_directory):
        os.mkdir("ImageInformation/" + file_directory)

try:
    img = Image.open(image_name)

    # Prints the needed information into the created file.
    with open("ImageInformation/" + file_name + ".txt", "w") as file:
        file.write(str(img.width) + " " + str(img.height) + "\n")
        # Defaults to writing the total image size, with one frame.
        if len(sys.argv) > 2:
            file.write(sys.argv[2] + " " + sys.argv[3] + "\n")
            file.write(sys.argv[4])
        else:
            file.write(str(img.width) + " " + str(img.height) + "\n")
            file.write(str(1))
except:
    print("Error creating file")
    raise

print("Successfully created ImageInformation/" + file_name + ".txt")