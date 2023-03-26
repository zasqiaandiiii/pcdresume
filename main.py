import cv2
import numpy as np
img = cv2.imread('arlo.jpg')
# mengubah format gambar dari BGR ke RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# mengubah format gambar ke bentuk array
img_arr = np.array(img)
# menghitung histogram gambar
hist, edges = np.histogramdd(img_arr.reshape(-1, 3), bins=(16, 16, 16), range=[(0, 255), (0, 255), (0, 255)])
# menemukan warna dominan
dominant_color = np.unravel_index(hist.argmax(), hist.shape)
red = edges[0][dominant_color[0]]
green = edges[1][dominant_color[1]]
blue = edges[2][dominant_color[2]]
# membuat kotak warna dominan
dominant_box = np.zeros((100, 100, 3), dtype=np.uint8)
dominant_box[:, :, 0] = blue
dominant_box[:, :, 1] = green
dominant_box[:, :, 2] = red
# menampilkan warna dominan dan gambar
print(f'Dominant color: RGB({red}, {green}, {blue})')
cv2.imshow('arlo', img)
cv2.imshow('Dominant color', dominant_box)
cv2.waitKey(0)
