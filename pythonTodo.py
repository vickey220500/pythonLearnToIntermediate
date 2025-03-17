import numpy
# import imutils as imgprocessing

# print(imgprocessing)
numArr = [1,2,3,4,5,6,7]
sumOfNa=0
print(len(numArr),'length of array')
# for loop 
for i in numArr: 
    sumOfNa+=i
    print(sumOfNa)

  
# mean function
def mean():
    sumOfNa=0 
    for i in numArr: 
        sumOfNa+=i
    return sumOfNa/len(numArr)

print(mean(),'mean')

# median function
