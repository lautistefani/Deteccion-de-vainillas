import cv2
import numpy as np



capture = cv2.VideoCapture(1)

#para ulitizar solo una porcion de la imagen se usa BELT belt=frame [Y:Y, X:X

while  True:
     _, frame = capture.read()

     frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     gauss = cv2.GaussianBlur(frame_grey, (15,15) ,0)

     _, threshold = cv2.threshold(gauss, 80,255, cv2.THRESH_BINARY)

     canny = cv2.Canny(threshold, 200,450)

  #  cv2.imshow("frame", frame)
  #   cv2.imshow("gris", frame_grey)
     cv2.imshow("Tresh", threshold)
     cv2.imshow("canny", canny)

     key = cv2.waitKey(1000)
     if key != (27):
         pass
     else:
         break

     (contornos, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     cv2.drawContours(frame, contornos, -1, (0, 0, 255), 2)
     cv2.imshow("contornos", frame)
     cv2.waitKey(1000)

     print("He encontrado {} objetos".format(len(contornos)))






capture.relase()
cv2.destroyAllWindows()