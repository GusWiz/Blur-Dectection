# Install openCV and watchdog packages using pip with "pip install opencv-python watchdog"
import cv2 
import numpy as np
import os
import time

# Funciton that detects if the image is blurry by using the Laplacian variance
def is_blurry(image_path, threshold = 100):
  img = cv2.imread(image_path)
  # Check worse case - No image is found
  if img is None:
    return None # No image/file was not found

  # Convert the image to grayscale
  gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # The code above is only necessary if we do NOT change the imread() parameter to read image 
  # with cv2.IMREAD_GRAYSCALE
  # Apply the Laplacian operator to detect for edges
  # the less amount of edges indicate a blurry image
  laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()

  # If the variance is below threshould (is smooth and lacks edges), it is considered blurry
  if laplacian_var < threshold: # Threshould can be adjusted if need be
    return True
  return False
  # You can replace last 3 lines with return laplacian_var < threshold

# Function that monitor folder for new images using OS library
def monitor_folder(folder_path, threshold = 100, intervals=1):
  # A set that contains the names of the files that have been processed/looked at
  processed_files = set()
  while True:
    for file_name in os.listdir(folder_path):
      if file_name not in processed_files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
          # You use the .add method to add a new element to a set
          processed_files.add(file_name)
          is_blurry_flag = is_blurry(file_path, threshold)
          if is_blurry_flag is not None:
            status = "Blurry" if is_blurry_flag else "Not Blurry"
            print(f"{file_name} is {status}")
          else:
            print(f"{file_name} not found")
    time.sleep(intervals)

# Running code
monitored_folder = "example/file/path"
blur_threshold = 100 # Adjust the threshold as needed
monitor_folder(monitored_folder, blur_threshold)