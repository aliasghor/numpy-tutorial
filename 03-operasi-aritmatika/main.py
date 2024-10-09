import numpy as np

# Penjumlahan dalam Built-in list Python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

for i in range(len(a)):
    hasil = a[i] + b[i]
    print(hasil)

# NumPy array
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Penjumlahan pada Python list
hasil_list = a + b

# Elementwise operation
# Penjumlahan
hasil_array = array1 + array2
print(hasil_array)

# Pengurangan
hasil_array = array1 - array2

# Pembagian
hasil_array = array1 / array2

# Perkalian
hasil_array = array1 * array2

# Kuadrat
hasil_array = array1**2

# Multi dimensi array numpy
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [-1, -2, -3]])

hasil_tambah_matrix = matrix1 + matrix2
hasil_kali_matrix = matrix1 * matrix2


# Display
print(hasil_kali_matrix)