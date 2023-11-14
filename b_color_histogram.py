import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def calculate_color_histogram(image):
    # Create a NumPy array from the image
    img_array = np.array(image)

    # Calculate the color histogram for each channel
    red_hist = np.histogram(img_array[:, :, 0], bins=256, range=(0, 256), density=True)
    green_hist = np.histogram(img_array[:, :, 1], bins=256, range=(0, 256), density=True)
    blue_hist = np.histogram(img_array[:, :, 2], bins=256, range=(0, 256), density=True)

    return red_hist, green_hist, blue_hist


# Load the image using Pillow
image_path = "/Users/bielohryvtsev/Image-Processing-with-Python/b_pic.png"  # Replace with the actual image file path
image = Image.open(image_path).convert("RGB")

# Calculate the color histogram for each channel
red_hist, green_hist, blue_hist = calculate_color_histogram(image)

# Plot the color histograms for each channel
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.plot(red_hist[1][:-1], red_hist[0], color='red')
plt.title("Red Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(3, 1, 2)
plt.plot(green_hist[1][:-1], green_hist[0], color='green')
plt.title("Green Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(3, 1, 3)
plt.plot(blue_hist[1][:-1], blue_hist[0], color='blue')
plt.title("Blue Channel Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()