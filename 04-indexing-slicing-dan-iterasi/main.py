import numpy as np

array = np.arange(10)
array2D = np.arange(16).reshape(4, 4)

print(array)
print(array2D)

# Mengambil nilai
print(f"Element ke 1 dari array = {array[0]}")
print(f"Element ke 1 dari array2D = {array2D[0, 0]}")
print(f"Element ke 7 dari array = {array[6]}")
print(f"Element terakhir dari array = {array[-1]}")
print(f"Element terakhir dari array2D = {array2D[3,-1]}")

# Indexing
print(f"Elemen array dari 1-6 adalah = {array[:6]}")
print(array2D[1:])
print(array2D[1:, :2])