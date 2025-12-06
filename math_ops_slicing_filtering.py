import numpy as np 

a = np.random.randint(1,100,20)
print(a)
print(a.mean())
print(a.sum())
print(a.min())
print(a.max())

a_mul_2 = a * 2
print(a_mul_2)

print(a - 10)

print(a[(a>60)]) #boolean filtering

a2 = np.random.randint(1,10,(10,10))
print(a2)
print(a2[3,3]) #indexing
print(a2[3:7,3:7]) #slicing
