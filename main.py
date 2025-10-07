import os
from PIL import Image

def adjust_brightness(img_path, brightness_percent):
    img = Image.open(img_path).convert("RGB")
    width, height = img.size
    new_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r = r + r * (brightness_percent / 100)
            g = g + g * (brightness_percent / 100)
            b = b + b * (brightness_percent / 100)
            r = max(0, min(255, int(r)))
            g = max(0, min(255, int(g)))
            b = max(0, min(255, int(b)))
            new_img.putpixel((x, y), (r, g, b))

    return new_img

file_path = input("Enter the path to file: ")

if not os.path.isfile(file_path):
    print("File not found.")
    exit(1)

try:
    percent = float(input("Enter percent to increase brightness of image: "))
except ValueError:
    print("Error occurred! Invalid number.")
    exit(1)

try:
    image = Image.open(file_path)
    print("Image successfully loaded.")
except Exception as e:
    print(f"Error loading image: {e}")
    exit(1)

modified_image = adjust_brightness(file_path, percent)

output_path = input("Enter path to save the modified image: ")

try:
    modified_image.save(output_path)
    print(f"Modified image saved to {output_path}.")
except Exception as e:
    print(f"Error saving image: {e}")
