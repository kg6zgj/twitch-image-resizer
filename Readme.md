# Image Resizer

This Python application automatically resizes images to square dimensions without stretching, centering the original image within the square, and then exports the resized images in multiple predefined sizes. This tool is particularly useful for preparing images for machine learning models, web applications, or any scenario requiring images of specific square dimensions.

## Features

- Converts any image to a square aspect ratio without distortion, centering it within the square.
- Exports images in multiple sizes: 28x28, 56x56, and 112x112 pixels.
- Supports PNG, JPEG, and JPG formats, ensuring exported PNGs have a transparent background.
- Processes all images in a specified directory automatically.

## Prerequisites

Before you start, make sure you have:

- Python 3.6 or higher installed on your system.
- The Pillow library for image processing.


## Install Prerequisites
pip install Pillow


## Usage

To use the Image Resizer, follow these steps:

1. Place all images you want to resize in a single directory (e.g., `images_to_process`).
2. Open `image_resizer.py` in your text editor and set the `folder_path` variable to the path of your images directory.
3. Run the script from your terminal or command prompt:
   1. ``python image_resizer.py``