import base64
import sys

def decode_and_save_file(base64_data, output_file):
    # Decode the base64 string
    file_contents = base64.b64decode(base64_data.encode('utf-8'))

    # Write the decoded file contents to the output file
    with open(output_file, 'wb') as file:
        file.write(file_contents)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decode_file.py base64_data output_file")
        sys.exit(1)
    
    base64_data = sys.argv[1]
    output_file = sys.argv[2]
    decode_and_save_file(base64_data, output_file)
