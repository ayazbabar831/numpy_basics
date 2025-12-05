import numpy as np

array1 = np.zeros((3,3))
array2 = np.ones((4,4))
array3 = np.full((3,5),9)
array4 = np.arange(1,10,3)
array5 = np.linspace(1,10,12)
print(array1)
print(array2)
print(array3)
print(array4)
print(array5)

I = np.zeros((5,5))
I[np.arange(5),np.arange(5)] += 1
print(I)

print(np.eye(5))
