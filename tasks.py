import numpy as np 

# Project 1 — Manual Grayscale Conversion Input: a 3D fake image array 
# (H,W,3) with random ints 0–255 
# Compute grayscale using only NumPy: 0.299*R + 0.587*G + 0.114*B 
# Output must be shape (H,W).

# H , W = 4,5
# img = np.random.randint(0,255,(H,W,3))
# print(img)
# grayscale = (img[:,:,0]*0.299) + (img[:,:,1]*0.587) + (img[:,:,2]*0.114)
# print(grayscale)

# Given 9 (64×64×3) random images: 
# reshape/concat them into a 3×3 grid → final shape 
# (192×192×3) No loops.

# img1 = np.random.randint(0,255,(64,64,3))
# img2 = np.random.randint(0,255,(64,64,3))
# img3 = np.random.randint(0,255,(64,64,3))
# img4 = np.random.randint(0,255,(64,64,3))
# img5 = np.random.randint(0,255,(64,64,3))
# img6 = np.random.randint(0,255,(64,64,3))
# img7 = np.random.randint(0,255,(64,64,3))
# img8 = np.random.randint(0,255,(64,64,3))
# img9 = np.random.randint(0,255,(64,64,3))

# row1 = np.hstack([img1,img2,img3])
# row2 = np.hstack([img4,img5,img6])
# row3 = np.hstack([img7,img8,img9])
# stack = np.vstack([row1,row2,row3])

# print(stack)

# Project 3 — Image Downscaler (No OpenCV) Given a 200×200 “image” (random): Reduce it to 100×100 by taking 
# every 2nd pixel Use slicing only. 

# img = np.random.randint(0,255,(200,200))
# print(img)
# downscaler = img[::2,::2]
# print(downscaler)


# Project 4 — Heatmap Normalizer Given 50×50 random floats: normalize values 
# between 0 and 1 apply threshold to highlight values > 0.8 count highlighted values 

array = np.random.random((50,50)) * 300
normal = (array-array.min())/(array.max()-array.min())
count = (normal > 0.8).sum()
print(count)

# Project 5 — Color Channel 
# Manipulation Given a 128×128×3 fake image: extract channels swap R and B merge back increase green channel by +50
# with clipping at 255 


# Project 6 — Image Padding With Concatenation Given a 64×64 image: pad with a 10-pixel border of white (255) 
# around all sides Use concatenate or pad.