import numpy as np

np.random.seed(42)
array = np.random.randint(1,50,(10,10))
print(array)
min = array.min()
max = array.max()
print(min,max)

v = np.random.randint(1,30,(30))
mean = v.mean()
print(mean)

a = np.ones((10,10))
a[1:-1,1:-1]  = 0
print(a)

b = np.arange(25).reshape((5,5))
print(np.pad(b,1))
zero = np.zeros((7,7))
print(b)
mid = b[1:-1,1:-1]
b = np.zeros((5,5))
b[1:-1,1:-1] = mid

zero[1:-1,1:-1] = b
print(b)
print(zero)

matrix = np.zeros((5,5))
matrix1 = np.arange(1,5)

print(matrix)
matrix[[1,2,3,4],[0,1,2,3]] = matrix1
print(matrix)
print(np.diag([1,2,3,4],k=-1))
print(np.diag(np.ones(5)))

rows= np.arange(8).reshape(1,8)
cols = np.arange(8).reshape(8,1)

q = (cols-rows)%2==0

print(q*1)

z = np.zeros((8,8))
z[::2,1::2] = 1
z[1::2,::2] = 1
print(z)



print(np.unravel_index(99,(6,7,8)))

np.random.seed()
y = np.random.randint(1,20,(4,4))

print((y-y.mean())/y.std())

h = np.arange(5*3).reshape(5,3)
i = np.arange(3*2).reshape(3,2)

ans = h@i
print(ans)
np.random.seed()

n = np.random.randint(1,20,20)

neg = np.where((n>=3)&(n<=8),n*(-1),n)
print(neg)