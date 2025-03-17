import cv2 as cv
import imutils # image manipulating
image = cv.imread('butterfly.jpeg')
resizeImg = imutils.resize(image,width=100)
gaussianImag = cv.GaussianBlur(image,(21,21),0) #smoothing image
grayimg = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
thresholdImg = cv.threshold(grayimg,180,255,cv.THRESH_BINARY)[1]
cv.imshow('show',image)
cv.imshow('showresize',resizeImg)
cv.imshow('gaussianImag',gaussianImag)
cv.imshow('thresholdImag',thresholdImg)
