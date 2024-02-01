import os
from PIL import Image


def resize_and_export(image_path, output_sizes=[28, 56, 112]):
    # Open the image
    image = Image.open(image_path)

    # Calculate the size for a square based on the largest dimension
    square_size = max(image.size)

    # Create a new, square image with transparent background
    new_image = Image.new('RGBA', (square_size, square_size), (0, 0, 0, 0))

    # Calculate the position to paste the original image on the new square canvas
    x = (square_size - image.size[0]) // 2
    y = (square_size - image.size[1]) // 2

    # Paste the original image onto the new square canvas
    new_image.paste(image, (x, y))

    # Resize and export for each specified size
    for size in output_sizes:
        resized_image = new_image.resize((size, size), Image.Resampling.LANCZOS)
        # Create a directory for each size if it doesn't exist
        output_dir = f'resized_{size}x{size}'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # Generate a new filename based on the original's
        base_name = os.path.basename(image_path)
        file_name, _ = os.path.splitext(base_name)
        output_path = os.path.join(output_dir, f'{file_name}_{size}x{size}.png')
        resized_image.save(output_path, format='PNG', optimize=True)
        print(f'Saved: {output_path}')


def process_folder(folder_path, output_sizes=[28, 56, 112]):
    for file_name in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        # Check if the file is an image (you might want to check for specific extensions)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                resize_and_export(file_path, output_sizes)
                print(f'Processed {file_name}')
            except Exception as e:
                print(f'Error processing {file_name}: {e}')


# Path to the folder containing images to process
folder_path = './images_to_process'  # Update this path to your folder's path
process_folder(folder_path)
