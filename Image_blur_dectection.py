# Install openCV and watchdog packages using pip with "pip install opencv-python watchdog"
import cv2 
import numpy as np

# Funciton that detects if the image is blurry by using the Laplacian variance
def is_blurry(image_path, threshold = 100):
  img = cv2.imread(image_path)
  # Check worse case - No image is found
  if img is None:
    return False

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

