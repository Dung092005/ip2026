import matplotlib.pyplot as plt
# Ma trận ảnh I (4x4)
I = [
    [0, 1, 1, 2],
    [2, 3, 3, 4],
    [4, 5, 6, 6],
    [5, 6, 7, 7]
]
rows = 4 
cols = 4
max_val = 7
# have 8 value from 0 - 7 
hist = [0]*8
for i in range(rows):
    for j in range(cols):
        v = I[i][j]
        hist[v] = hist[v] + 1

# normalization
normal = [0] * 8
for i in range(8):
    normal[i] = hist[i] / 16

# histogam equalization 

cdf = 0
s_k = [0] * 8 
for k in range(8):
    cdf = cdf + normal[k]
    s_k[k] = round(cdf * max_val)           # Nhân (L-1) và làm tròn


M = [[0] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        old_value = I[i][j]
        new_value = s_k[old_value]
        M[i][j] = new_value

#  Convert image I into a binary image B using thresholding, where predefined threshold k is selected as the median gray-level value of all pixels in image I.
# take 4 as thearedhold
k = 4
B = [[0] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if I[i][j] < k:
            B[i][j] = 0
        else:
            B[i][j] = 1


# - Compute negative image of I
I_nega = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        I_nega[i][j] = 7 - I[i][j]
        
gray_level = [0, 1, 2, 3, 4, 5, 6, 7]
# draw histogam
plt.bar(gray_level, hist)
plt.title("Histogram of image I")
plt.xlabel("Gray level")
plt.ylabel("Number of pixels")
plt.show()
# normalized histogram of image I
plt.bar(gray_level, normal)
plt.title("Normalized histogram of image I")
plt.xlabel("Gray level")
plt.ylabel("Probability")
plt.show()
# histogram of equalized image M
plt.bar(gray_level, normal)
plt.title("Normalized histogram of image I")
plt.xlabel("Gray level")
plt.ylabel("Probability")
plt.show()

# draw histogam of equalization 
plt.bar(gray_level,s_k)
plt.title("")
plt.xlabel("Gray level")
plt.ylabel("equalization of histogram")
plt.show()




