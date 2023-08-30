import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C://Users//STAR//Pictures//OIP0.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_array = np.array(histogram)
plt.figure(figsize=(8, 6))
plt.plot(hist_array, color='black')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Image Histogram')
plt.xlim([0, 256])
plt.show()
