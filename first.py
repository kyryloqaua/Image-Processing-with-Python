import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def calculate_color_histogram(image):
    # Create a NumPy array from the image
    img_array = np.array(image)

    # Calculate the color histogram
    histogram = np.histogram(img_array, bins=256, range=(0, 256), density=True)

    return histogram


def calculate_power_spectrum(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Calculate the power spectrum
    power_spectrum = np.abs(np.fft.fftshift(np.fft.fft2(grayscale_image))) ** 2

    return power_spectrum


# Load the image using Pillow
image_path = "/Users/bielohryvtsev/Image-Processing-with-Python/pic_2.jpg"  # Replace with the actual image file path
image = Image.open(image_path).convert("RGB")

# Calculate the color histogram
color_histogram = calculate_color_histogram(image)

# Calculate the power spectrum
power_spectrum = calculate_power_spectrum(image)

# Plot the color histogram
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(color_histogram[1][:-1], color_histogram[0], color='black')
plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

# Plot the power spectrum
plt.subplot(2, 1, 2)
plt.imshow(np.log10(power_spectrum), cmap='gray')
plt.title("Power Spectrum")
plt.axis('off')

plt.tight_layout()
plt.show()