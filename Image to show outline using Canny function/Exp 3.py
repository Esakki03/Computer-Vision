{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "63f768c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1 1 1]\n",
      " [1 1 1 1 1]\n",
      " [1 1 1 1 1]\n",
      " [1 1 1 1 1]\n",
      " [1 1 1 1 1]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "91"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "kernel = np.ones((5,5),np.uint8)\n",
    "print(kernel)\n",
    "path = \"C:/Users/STAR/Pictures/OIP.jpg\"\n",
    "img =cv2.imread(path)\n",
    "imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)\n",
    "imgCanny = cv2.Canny(imgBlur,100,200)\n",
    "cv2.imshow(\"Img Canny\",imgCanny)\n",
    "cv2.waitKey(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b44ff55",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
