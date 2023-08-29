import cv2
import numpy as np
image_path = "C://Users//STAR//Pictures//OIP1.jpg"
image = cv2.imread(image_path)
x = 100
y = 150
w = 300
h = 250
mask = np.zeros(image.shape[:2], np.uint8)
rect = (x, y, w, h)
cv2.grabCut(image, mask, rect, None, None, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = image * mask2[:, :, np.newaxis]
cv2.imshow('Background Removed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
