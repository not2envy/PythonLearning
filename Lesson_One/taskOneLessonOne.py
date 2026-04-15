myList = [1,25,69,72,50,61,75,83,16]

#checking all numbers in list myList for > 50 assigning it to bigNumbers list
bigNumbers = [num for num in myList if num > 50]

#squaring numbers in the list with in bigNumbers
squaredBigNumbers = [sqr**2 for sqr in bigNumbers]

print((squaredBigNumbers))
