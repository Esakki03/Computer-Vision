{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "877390b9",
   "metadata": {},
   "outputs": [
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
    "path = \"C:/Users/STAR/Pictures/OIP.jpg\"\n",
    "src = cv2.imread(path)\n",
    "window_name = 'Image'\n",
    "image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)\n",
    "cv2.imshow(window_name, image)\n",
    "cv2.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae9795a8",
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
