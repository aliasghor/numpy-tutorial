import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Membuat matrix dengan ukuran: {a.shape}")
print(a)

# Transpose matrix
print("Transpose matrix dari a:")
# print(a.transpose())
# print(np.transpose(a))
print(a.T)

# Flatten array, vector baris
print("Flatten matrix a:")
print(np.ravel(a))
# print(a.ravel())

# Reshape matrix
print("Reshape matrix a:")
# print(a.reshape(3, 2))
print(np.reshape(a, (3, 2)))
print(f"Ukuran matrix setelah direshape: {a.shape}")

# Resize matrix
print("Resize matrix a:")
a.resize(3, 2)
print(a)
print(f"Ukuran matrix setelah diresize: {a.shape}")
