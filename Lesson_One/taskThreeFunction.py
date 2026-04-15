import statistics
#function  using Statistic import to get the average
def averageNumbers(list):
    return statistics.mean(list)

myList = [1,25,69,72,50,61,75,83,16]
result = averageNumbers((myList))
print(result)