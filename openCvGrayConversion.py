import cv2 as cv
image = cv.imread('butterfly.jpeg')
grayimg = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('show',image)
cv.imshow('showGray',grayimg)
print(image.size) #32978 pixel size
print(image.shape)  #(148, 199, 3) -> (row,column,color)