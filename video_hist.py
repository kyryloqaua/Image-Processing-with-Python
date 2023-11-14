import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_color_histogram(frame):
    # Calculate the color histogram for each channel
    red_hist = np.histogram(frame[:, :, 0], bins=256, range=(0, 256), density=True)
    green_hist = np.histogram(frame[:, :, 1], bins=256, range=(0, 256), density=True)
    blue_hist = np.histogram(frame[:, :, 2], bins=256, range=(0, 256), density=True)

    return red_hist, green_hist, blue_hist

# Open the video file
video_path = "/Users/bielohryvtsev/Image-Processing-with-Python/video.mp4"  # Replace with the actual video file path
video = cv2.VideoCapture(video_path)

# Calculate histograms for each frame in the video
frame_count = 0
timestamps = []
red_values = []
green_values = []
blue_values = []

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Convert the frame to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Calculate the color histogram for the frame
    red_hist, green_hist, blue_hist = calculate_color_histogram(frame)

    # Append the histogram values for each channel to the respective lists
    timestamps.append(frame_count)
    red_values.append(red_hist[0])
    green_values.append(green_hist[0])
    blue_values.append(blue_hist[0])

    frame_count += 1

# Plot the color histograms over time
plt.figure(figsize=(8, 6))
plt.plot(timestamps, red_values, color='red', label='Red Channel', alpha=0.7)
plt.plot(timestamps, green_values, color='green', label='Green Channel', alpha=0.7)
plt.plot(timestamps, blue_values, color='blue', label='Blue Channel', alpha=0.7)

plt.title("Color Channel Histograms over Time")
plt.xlabel("Frame Number")
plt.ylabel("Frequency")
# Adjust the legend location if needed

plt.show()

# Release the video capture
video.release()
cv2.destroyAllWindows()
