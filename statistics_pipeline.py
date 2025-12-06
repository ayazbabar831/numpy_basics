import numpy as np

# array = np.random.randint(1,100,(100,100))
# a_mean = array.mean()
# a_std = array.std()

# normalize = (array-a_mean)/a_std
# print(normalize)

# a = np.arange(16).reshape((4,4))
# w = np.array([0.1, 0.2, 0.3, 0.2])
# rowwise_sum = a.sum(axis=1,keepdims=True)
# w_mul_a = w*a
# print(w_mul_a)
# print(a)
# print(a.sum())
# print(rowwise_sum)
# print(a+rowwise_sum)

X = np.array([
    [12.5, 7.8, 105.0, 3, 0.5],
    [15.2, 9.1, 88.5,  5, 0.8],
    [11.0, 6.5, 112.0, 4, 0.4],
    [13.8, 8.2, 95.0,  3, 0.9],
    [16.0, 10.5, 101.5, 6, 0.7],
    [10.1, 7.1, 99.0,  4, 0.3]
])
mean_of_X = X.mean()
mask1 = X < 5
mask2 = X>15
X[mask1] = mean_of_X
X[mask2] = 15
print(X)

data1 = X[:,:3]
d1_min = data1.min(axis=0,keepdims=True)
d1_max = data1.max(axis=0,keepdims=True)
normal = (data1 - d1_min)/(d1_max - d1_min)
print(normal)


data2 = X[:,3:]
d2_mean = data2.mean(axis=0,keepdims=True)
d2_std = data2.std(axis=0,keepdims=True)
z_score = (data2 - d2_mean)/d2_std

print(np.hstack([normal,z_score]))

print(X)