import cv2 as cv

img = cv.imread('userImg.png')
cv.imshow('User Image',img)
cv.imwrite('user.jpg',img)

cv.waitKey(5000)
cv.destroyAllWindows()
