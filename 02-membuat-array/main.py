# 2. Membuat NumPy (Numerical Python) array
import numpy as np

# Membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Membuat vector dengan range (jarak)
c = np.arange(0, 10, 2)

# Membuat array dengan linspace
d = np.linspace(0, 10, 6)

# Membuat array multidimensi
e = np.array([
    (1, 2, 3),
    (4, 5, 6)
])

# Matrix dengan nilai nol
f = np.zeros((3, 4))

# Matrix dengan nilai satu
g = np.ones((6, 3))

# Matrix identitas
h = np.identity(5)
i = np.eye(5)

# Display
print(h)