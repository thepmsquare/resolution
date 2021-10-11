from PIL import Image
import random

default_width = 1920
default_height = 1080


def create_image(width=default_width, height=default_height):

    im = Image.new("RGB", (width, height), "#000000")
    pixels = im.load()
    for i in range(0, width):
        for j in range(0, height):
            pixels[i, j] = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
    im.show()
    im.save("resolution.png")
    print("Image created.")


if __name__ == "__main__":
    try:
        width = int(input("Width: "))
        height = int(input("Height: "))
        create_image(width, height)
    except:
        print(
            f"Incorrect input, generating image with default values. Width = {default_width}, Height = {default_height}.")
        create_image()
