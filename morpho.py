import cv2
import numpy as np

img = cv2.imread('bw.png',0)
kernel = np.ones((5,5),np.uint8)

# Erosion
erosion = cv2.erode(img,kernel,iterations = 1)
com_ero = np.hstack((img,erosion))
cv2.imwrite('Erosion1.jpg',erosion)
cv2.imwrite('compare erosion.png',com_ero)

# Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)
com_dil = np.hstack((img,dilation))
cv2.imwrite('Dilation1.jpg',dilation)
cv2.imwrite('compare dilation.png',com_dil)

result = np.stack((img,erosion,dilation))
cv2.imwrite('result.jpg',result)


