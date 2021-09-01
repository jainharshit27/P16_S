dict1 = 'a': 100, 'b':200, 'c':300

def returnSum(myDict):
      
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
      
    return sum
  
print("Sum :", returnSum(dict1))
