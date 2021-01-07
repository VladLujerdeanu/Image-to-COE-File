import numpy as np
import sys
import os
from PIL import Image

def img2coe(path, index):
    img = Image.open(path)
    arr = np.array(img)

    output_file = "img" + str(index) + ".coe"

    f = open(output_file, "w")

    f.write("memory_initialization_radix=2;\nmemory_initialization_vector=")

    for line in arr:
        for r, g, b in line:
            r = int((r * 16) / 256)
            g = int((g * 16) / 256)
            b = int((b * 16) / 256)
            f.write(str('\n{:04b}'.format(r)) + str('{:04b}'.format(g)) + str('{:04b}'.format(b)) + ",")
    f.seek(f.tell() - 1, os.SEEK_SET)
    f.truncate()
    f.write(";")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            img2coe(str(sys.argv[i]), i)
    else:
        print("Insert at least one image path\nFormat: python img2coe.py <path>")