import cv2
import pytesseract
from PIL import Image

def detect_text(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use thresholding to preprocess the image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use pytesseract to do OCR on the thresholded image
    pil_image = Image.fromarray(thresh)
    text = pytesseract.image_to_string(pil_image, lang='eng')


    return text

# Path to the image file
image_path = "/Users/bielohryvtsev/Image-Processing-with-Python/text_zoox.jpeg"  # Replace with the actual path to your image

# Detect text in the image
detected_text = detect_text(image_path)

# Print the detected text
print("Detected Text:")
print(detected_text)
