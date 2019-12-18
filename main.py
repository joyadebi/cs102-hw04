import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")


for i in range(1, width // 2):
    for j in range(1, height // 2):
        r, g, b = img.getpixel((i, j))
        if b < 100:
            b = b + 150
        if 100 < b < 150:
            b = b + 75
        if 150 < r < 200:
            r = r + 25
        if g > 125:
            g = g + 125
        if r > 125:
            r = r - 125
        new_img.putpixel((i, j), (r, g, b))

for i in range(width // 2, width):
    for j in range(1, height // 2):
        r, g, b = img.getpixel((i, j))
        if g < 100:
            g = g + 150
        if 100 < g < 150:
            g = g + 75
        if 150 < b < 200:
            b = b + 25
        if g > 125:
            g = g - 125
        if b > 125:
            b = b - 125
        new_img.putpixel((i, j), (r, g, b))

for i in range(width // 2, width):
    for j in range(height // 2, height):
        r, g, b = img.getpixel((i, j))
        if b < 100:
            b = b + 150
        if 100 < b < 150:
            b = b + 75
        if 150 < r < 200:
            r = r + 25
        if g > 125:
            g = g + 125
        if r > 125:
            r = r - 125
        new_img.putpixel((i, j), (r, g, b))

for i in range(1, width // 2):
    for j in range(height // 2, height):
        r, g, b = img.getpixel((i, j))
        if g < 100:
            g = g + 150
        if 100 < g < 150:
            g = g + 75
        if 150 < b < 200:
            b = b + 25
        if g > 125:
            g = g - 125
        if b > 125:
            b = b - 125
        new_img.putpixel((i, j), (r, g, b))

new_img.save(output_path, "JPEG")

