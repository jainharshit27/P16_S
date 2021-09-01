dict1 = {'a': 100, 'b':200, 'c':300}

def returnSum(myDict):
      
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
      
    return sum
  
sum = returnSum(dict1)
print("Sum :", sum)
