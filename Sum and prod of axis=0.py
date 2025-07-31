import numpy as np
n,m = map(int,input("enter 2 nums").split()) #to get number of rows and columns

array = np.array([list(map(int,input().split())) for i in range(n)])
#to enter elements of the array
sum = np.sum(array,axis=0)
#to sum along the columns
result = np.prod(sum)
#sum of columns is multiplied
print(result)
#axis =0 means sum along columns 1 and 2