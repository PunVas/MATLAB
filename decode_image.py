import base64
import sys

def decode_image(input_file, output_file):
    with open(input_file, 'r') as file:
        base64_data = file.read()
    # Remove data URL prefix if present
    if ',' in base64_data:
        base64_data = base64_data.split(',')[1]
    image_data = base64.decodebytes(base64_data.encode('utf-8'))
    with open(output_file, 'wb') as file:
        file.write(image_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decode_image.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    decode_image(input_file, output_file)
