import cv2
image = cv2.imread("C://Users//STAR//Pictures//OIP0.jpg")
text = "MS DHONI"
position = (150, 300)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 0)
a=cv2.putText(image, text, position, font, font_scale, font_color, 2)
cv2.imshow('output_image.jpg', a)
cv2.waitKey(0)
cv2.destroyAllWindows()