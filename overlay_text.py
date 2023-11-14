import numpy as np
from PIL import Image, ImageDraw, ImageFont

def overlay_text(image_path, text, output_path):
    # Load the image using Pillow
    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    
    # Create a NumPy array from the image
    img_array = np.array(image)
    
    # Create a PIL ImageDraw object to draw the text on the image
    draw = ImageDraw.Draw(image)
    
    # Specify the font and size for the text
    font_path = "/Users/bielohryvtsev/Image-Processing-with-Python/amatic/AmaticSC-Regular.ttf"  # Replace with the path to your font file
    font_size = 100
    font = ImageFont.truetype(font_path, font_size)
    
    # Specify the position where the text should be placed
    text_position = (1500, 1200)
    
    # Specify the color for the text (in RGB format)
    text_color = (255, 0, 0)  # Red color
    
    # Draw the text on the image
    draw.text(text_position, text, font=font, fill=text_color)
    
    # Save the modified image
    image.save(output_path)
    
    print("Text overlay completed.")

# Example usage
image_path = "/Users/bielohryvtsev/Image-Processing-with-Python/pic_1.png"  # Replace with the path to your image file
text = "ZOOX!"
output_path = "/Users/bielohryvtsev/output_image.jpg"  # Replace with the desired output path

overlay_text(image_path, text, output_path)