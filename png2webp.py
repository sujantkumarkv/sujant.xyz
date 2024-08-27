from PIL import Image
import os

def convert_png_to_webp(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG image
        if filename.endswith(".png"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Open the image file
            image = Image.open(file_path)
            # Define the output filename with the new extension
            output_filename = filename[:-4] + '.webp'
            # Save the image in WEBP format with specified quality
            image.save(os.path.join(directory, output_filename), 'WEBP', quality=90)
            # Optional: Remove the original PNG file
            os.remove(file_path)

# Usage
convert_png_to_webp('./static/assets/notes')

# def convert_png_to_ico(png_path, ico_path):
#     # Open the PNG image file
#     image = Image.open(png_path)
#     # Save the image in ICO format
#     image.save(ico_path, format='ICO')

# # Define the paths for the input PNG and output ICO files
# png_path = './static/favicon.png'
# ico_path = './static/favicon.ico'

# # Convert the PNG to ICO
# convert_png_to_ico(png_path, ico_path)


