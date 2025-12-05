import numpy as np
a = np.array([[18, 11, 19, 14,  5],
              [16,  8, 17,  5, 10],
              [ 7, 13, 11,  6, 17],
              [ 1, 19, 20, 15,  9],
              [ 4, 12,  2, 18, 14]])

# w = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# weighted_mean = (a*w).sum(axis=1)/w.sum()
# print(weighted_mean)

# less_then_10 = a[(a<10)]
# print(less_then_10)

# b = a.copy()
# max_mask = b.max(axis=1)>15
# print(max_mask)
# b[max_mask] = b[max_mask] -10
# print(b)

# c = a.copy()
# mask = c<5
# c[mask] = 0
# print(c)

d = a.copy()
greater_than_15_mask = a>15
d[greater_than_15_mask] = 50
print(d)

math_op = (a*a) - (10*a)
print(math_op)

colomn_wise_mean = a.mean(axis=0,keepdims=True)
z_score = (a - colomn_wise_mean)/a.std(axis=0,keepdims=True)
print(z_score)