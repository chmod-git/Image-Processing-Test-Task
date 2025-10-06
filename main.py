import os
from PIL import Image
file_path = input("Enter the path to file: ")

if not os.path.isfile(file_path):
    print("File not found.")
    exit(1)
try:
    percent = float(input("Enter percent to increase brightness of image: "))
except ValueError:
    print("Error occured!")
    exit(1)


try:
    image = Image.open(file_path)
    print("Image successfully loaded.")
except Exception as e:
    print(f"Error loading image: {e}")
    exit(1)


output_path = input("Enter path to save the modified image: ")


try:
    modified_image.save(output_path)
    print(f"Modified image saved to {output_path}.")
except Exception as e:
    print(f"Error saving image: {e}")