import cv2
from numpy import*

i=cv2.imread('go vegeta.jpg')
rImage=cv2.resize(i,(100,50))
cv2.imshow('frame',rImage)
cv2.waitKey(0)
cv2.destroyAllWindows()