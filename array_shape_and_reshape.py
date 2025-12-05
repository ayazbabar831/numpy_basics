import numpy as np

array = np.random.randint(1,20,(3,4))

array_shape = np.shape(array)
print(array_shape)

array_reshape = array.reshape(6,2)
array_reshape_shape = np.shape(array_reshape)
print(array_reshape_shape)
print(array_reshape)

a = np.arange(10)
a2d = a.reshape(5,2)
print(np.shape(a2d))
print(a2d)

flatten_a2d = a2d.flatten()
print(np.shape(flatten_a2d))
print(flatten_a2d)