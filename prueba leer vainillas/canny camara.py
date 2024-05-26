import cv2
import numpy as np

vainilla = cv2.imread("2.jpg")



grey = cv2.cvtColor(vainilla, cv2.COLOR_BGR2GRAY)


thras = cv2.threshold(grey , 150, 200, cv2.THRESH_BINARY)


canny = cv2.Canny(thras, 20,450)

cv2.imshow("contornos", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
