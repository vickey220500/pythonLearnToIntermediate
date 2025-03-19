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
# cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) Thickess code
# cv.putText(img,text,(10,20),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2) Text generator 
# cv.findContours(threshImg.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) its for get the border of the object
