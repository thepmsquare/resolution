from PIL import Image
import random
width = 1920
height = 1080
im = Image.new("RGB", (width, height), "#000000")
pixels = im.load()
for i in range(0, width):
    for j in range(0, height):
        pixels[i, j] = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
im.show()
im.save("resolution.tiff")
