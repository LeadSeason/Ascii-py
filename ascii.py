import math
import pathlib
import argparse
import numpy as np
from PIL import Image
from termColor import RGBtoEscape

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--chars", help="Characters to be used in ascii art", default="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
parser.add_argument("-s", "--scale", type=float, default=0.08)
parser.add_argument("-b", "--brightness", type=float, default=1.5)
parser.add_argument("convert_file", type=pathlib.Path, help="image file to be converted")
args = parser.parse_args()

# charsString = "█▓░ "
charsString = args.chars
Scalefactor = args.scale
image_path = args.convert_file
chars = list("".join(reversed(charsString)))


def BritnessToChar(h):
    points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    t = np.linspace(0, 1, 256)
    curve = np.array([(1 - t)**3, 3 * (1 - t)**2 * t, 3 * (1 - t) * t**2, t**3]).T
    bezier_values = np.dot(curve, points)

    h = bezier_values[math.floor(h)][1] * 255

    charslen = len(chars)
    mul = charslen / 256

    return chars[math.floor(h * mul)]


with Image.open(image_path) as img:

    imgWidth, imgHeight = img.size

    imgWidthScalefactor = int(imgWidth * Scalefactor)
    imgHeightScalefactor = int(imgHeight * Scalefactor)

    img = img.resize(
        (imgWidthScalefactor, imgHeightScalefactor),
        Image.NEAREST
    )

    # Fix rotation and flip
    img = img.transpose(2)
    img = img.transpose(0)
    img = img.transpose(2)
    img = img.transpose(2)

    imgWidth, imgHeight = img.size

    imgPixel = img.load()


for x in range(imgHeight):
    buffer = ""
    for y in range(imgHeight):
        red, green, blue, alpha = imgPixel[x, y]
        grey = int((red / 3 + green / 3 + blue / 3))
        char = BritnessToChar(grey)
        buffer += RGBtoEscape([red, green, blue]) + char * 2
    print(buffer)
