import cv2
import numpy as np

# mengonversi gambar dari RGB ke CIELAB
def rgb2lab(rgb_img):
    lab_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2LAB)
    return lab_img
# membaca gambar
img = cv2.imread('arlo.jpg')
img = cv2.resize(img, (326, 536))

# mengonversi gambar dari RGB ke CIELAB
lab_img = rgb2lab(img)

# menampilkan gambar
cv2.imshow("RGB Image", img)
cv2.imshow("CIELAB Image", lab_img)

# menunggu tombol keyboard ditekan
cv2.waitKey(0)

# menutup jendela
cv2.destroyAllWindows()