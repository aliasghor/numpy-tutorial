import numpy as np

# Concatenate 2 buah array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)

# Concatenate 2 buah matrix
matrix_pertama = np.array([[1, 2, 3], [4, 5, 6]])
matrix_kedua = np.array([[7, 8, 9], [10, 11, 12]])
matrix_gabungan = np.concatenate((matrix_pertama, matrix_kedua), axis=1)
print("Matrix pertama:")
print(matrix_pertama)

print("Matrix kedua:")
print(matrix_kedua)

print("Matrix gabungan:")
print(matrix_gabungan)

# Stacking matrix (Menumpuk matrix)
horizontal_matrix = np.hstack((matrix_pertama, matrix_kedua))
print("Horizontal matrix:")
print(horizontal_matrix)

vertical_matrix = np.vstack((matrix_pertama, matrix_kedua))
print(vertical_matrix)