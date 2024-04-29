import os
import base64
from PIL import Image

def decode_and_save_image(input_file, output_file):
    # Read binary data from the input file
    with open(input_file, 'rb') as f:
        binary_data = f.read()

    # Convert binary data to image using PIL
    image = Image.open(io.BytesIO(binary_data))

    # Save the image as PNG
    image.save(output_file, format="PNG")

if __name__ == "__main__":
    import sys
    import io
    import yaml

    # Load YAML configuration
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    # Ensure decoded images directory exists
    os.makedirs(config['decoded_images_dir'], exist_ok=True)

    # Iterate through each binary file in the specified directory
    for filename in os.listdir(config['input_images_dir']):
        if filename.endswith('.txt'):
            input_file = os.path.join(config['input_images_dir'], filename)
            output_file = os.path.join(config['decoded_images_dir'], f"{os.path.splitext(filename)[0]}.png")
            decode_and_save_image(input_file, output_file)
