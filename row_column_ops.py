import numpy as np

a = np.random.randint(1,30,(5,5))
print(a)
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.max(axis=1))
print(a.max(axis=0))
print(a.min(axis=1))
print(a.min(axis=0))
print(a.mean(axis=1))
print(a.mean(axis=0))

row_mean = a.mean(axis=1,keepdims=True)
print(a - row_mean)

row_min = a.min(axis=1,keepdims=True)
row_max = a.max(axis=1,keepdims=True)
row_mean = a.mean(axis=1,keepdims=True)
row_std = a.std(axis=1,keepdims=True)

print((a-row_min)/(row_max - row_min))
print((a-row_mean)/row_std)
mask1 = a.sum(axis=1) > 50
print(a[mask1])

mask2 = a%2
print(mask2)