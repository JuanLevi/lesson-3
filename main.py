import cv2
import numpy

duck=cv2.imread('images\daffyduck.jpg')
land=cv2.imread('images\landscape.png')


#grayscale
grey=cv2.cvtColor(land,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',grey)
cv2.waitKey(500)

#hsv
hsv=cv2.cvtColor(land,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
cv2.waitKey(500)


row,col=land.shape[0:2]
for i in range(row):
    for j in range(col):
        land[i,j]=sum(land[i,j])*0.33
cv2.imshow('gray',land)
cv2.waitKey(500)


#rotate
rotate=cv2.rotate(duck,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('rotate',rotate)
cv2.waitKey(500)

#custom rotation
row,col=duck.shape[0:2]
m=cv2.getRotationMatrix2D((col/2,row/2),30,1)
rotate=cv2.warpAffine(duck,m,(col,row))
cv2.imshow('custom rotate',rotate)
cv2.waitKey(500)

#edge detection
edges1=cv2.Canny(duck,100,500)
cv2.imshow('edges detection',edges1)
cv2.waitKey(5000)

#edge detection
edges2=cv2.Canny(land,10,50)
cv2.imshow('edges detection',edges2)
cv2.waitKey(5000)