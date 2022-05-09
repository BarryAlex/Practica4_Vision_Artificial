#Edwing Alexis Casillas Valencia.   19110113.   7E1.    Práctica 4 visión artificial

import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as img

r=1

imagen=np.zeros((400,600,3),dtype=np.uint8)
cv2.imwrite('Imagen.png',imagen)

#Dibujo
cv2.line(imagen,(40,40),(120,120),(125,200,35),4)
cv2.rectangle(imagen,(255,300),(350,380),(0,125,250),-3)
cv2.circle(imagen,(300,150),100,(0,0,255),4)
cv2.circle(imagen,(300,150),70,(0,255,0),4)
cv2.circle(imagen,(300,150),40,(255,0,255),4)
cv2.circle(imagen,(300,150),10,(0,255,255),-4)
cv2.putText(imagen,'"Inserte frase tipica de programacion"',(350,20),2,0.38,(255,125,180),1,cv2.LINE_AA)
#Monito
cv2.circle(imagen,(480,290),20,(0,255,255),-1)
cv2.line(imagen,(480,290),(480,370),(0,255,255),4)
cv2.line(imagen,(450,330),(510,330),(0,255,255),4)
cv2.line(imagen,(480,370),(450,400),(0,255,255),4)
cv2.line(imagen,(480,370),(510,400),(0,255,255),4)
cv2.imwrite('Dibujo.png',imagen)

while(r==1):
    #ROI
    roi=cv2.selectROI(imagen,showCrosshair=False,fromCenter=False)
    print(roi)
    print('')
    #Crop selected roi from raw image
    roi_cropped=imagen[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    cv2.imwrite('Imagen_ROI.png',roi_cropped)

    #cv2.imshow('Imagen',imagen)
    cv2.imshow('ROI',roi_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    r=int(input('Presione 1 para volver a realizar la accion\nPresione cualquier numero diferente de 1 para salir\n'))
    print('')
