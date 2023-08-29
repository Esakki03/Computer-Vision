import cv2
import numpy as np
image = cv2.imread("C://Users//STAR//Pictures//OIP0.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel_size = (5, 5)
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
smoothed_image = cv2.filter2D(gray_image, -1, kernel)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
median_blurred_image = cv2.medianBlur(gray_image, 5)
bilateral_filtered_image = cv2.bilateralFilter(gray_image, 9, 75, 75)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Gaussian Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()