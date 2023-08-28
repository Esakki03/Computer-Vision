{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36ec51b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "img = cv2.imread(\"C:/Users/STAR/Pictures/OIP.jpg\")\n",
    "rows,cols,ch = img.shape\n",
    "pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])\n",
    "pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])\n",
    "M = cv2.getPerspectiveTransform(pts1,pts2)\n",
    "dst = cv2.warpPerspective(img,M,(cols, rows))\n",
    "cv2.imshow('Transformed Image', dst)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb410c99",
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
