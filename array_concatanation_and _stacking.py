import numpy as np

A = np.arange(12).reshape(3,4)
B = np.ones((3,4), dtype=int)

c = np.vstack([A,B])
d = np.hstack([A,B])
e = np.stack([A,B],axis=0)
print(c)
print(d)
print(e)

x = np.array([1,2,3,4])
y = np.array([10,20,30,40])

z = np.stack([x,y],axis=1).flatten()
print(z)

arr = np.array([
    [12, 7, 1],
    [5,  20, 2],
    [9,  15, 3],
    [21, 8, 4]
])

mask = (arr[:,0]>10) & (arr[:,1] < 10)
print(arr[mask])

a = np.zeros((3,3))
b = np.ones((3,5))
c = np.arange(16).reshape(2,8)

top = np.hstack([a,b])
final = np.vstack([top,c])
print(final)


u = np.random.randint(0,20,(10,10))
print(u)
mask1 = u<10
mask2 = (u >= 10) & (u < 15)
mask3 = u >= 15

u[mask1] = 0
u[mask2] = 1
u[mask3] = 2
print(u)

block = np.array([[1,0],[0,1]])
check = np.tile(block,[3,3])
check_5xt = check[:5,:5]
print(check_5xt)

rows = np.arange(5).reshape(5,1)
cols = np.arange(5).reshape(1,5)

checker = (rows-cols) % 2
print(checker)