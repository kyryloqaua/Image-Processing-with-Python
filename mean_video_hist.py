import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_intensity(frame):
    # Calculate the intensity level for each channel
    red_intensity = np.mean(frame[:, :, 0])
    green_intensity = np.mean(frame[:, :, 1])
    blue_intensity = np.mean(frame[:, :, 2])

    return red_intensity, green_intensity, blue_intensity

# Open the video file
video_path = "/Users/bielohryvtsev/Image-Processing-with-Python/video.mp4"  # Replace with the actual video file path
video = cv2.VideoCapture(video_path)

# Initialize empty lists to store intensity levels over time
timestamps = []
red_intensity = []
green_intensity = []
blue_intensity = []

# Calculate intensity levels for each frame in the video
frame_count = 0

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Convert the frame to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Calculate the intensity levels for the frame
    red_int, green_int, blue_int = calculate_intensity(frame)

    # Append intensity levels to the respective lists
    timestamps.append(frame_count)
    red_intensity.append(red_int)
    green_intensity.append(green_int)
    blue_intensity.append(blue_int)

    frame_count += 1

# Plot intensity levels over time
plt.figure(figsize=(8, 6))
plt.plot(timestamps, red_intensity, color='red', label='Red Channel')
plt.plot(timestamps, green_intensity, color='green', label='Green Channel')
plt.plot(timestamps, blue_intensity, color='blue', label='Blue Channel')

plt.title("Intensity Levels over Time")
plt.xlabel("Frame Number")
plt.ylabel("Intensity Level")
plt.legend()

plt.show()

# Release the video capture
video.release()
cv2.destroyAllWindows()