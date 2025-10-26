import math
import numpy as num

l1 = int(input("Masukkan panjang lengan pertama (l1): "))
l2 = int(input("Masukkan panjang lengan kedua (l2): "))
# menambahkan degree of freedom ketiga
l3 = int(input("Masukkan panjang lengan ketiga (l3): "))

t1 = int(input("Masukkan sudut servo 1 dalam derajat (t1): "))
t2 = int(input("Masukkan sudut servo 2 dalam derajat (t2): "))
t3 = int(input("Masukkan sudut servo 3 dalam derajat (t3): "))

t1 = math.radians(t1)
t2 = math.radians(t2)
t3 = math.radians(t3)
cos_t1 = math.cos(t1)
sin_t1 = math.sin(t1)
cos_t2 = math.cos(t2)
sin_t2 = math.sin(t2)
cos_t3 = math.cos(t3)
sin_t3 = math.sin(t3)


mat1 = [
    [cos_t1, -sin_t1, 0],
    [sin_t1, cos_t1, 0],
    [0, 0, 1],
]
mat2 = [
    [1, 0, l1],
    [0, 1, 0],
    [0, 0, 1],
]
mat3 = [
    [cos_t2, -sin_t2, 0],
    [sin_t2, cos_t2, 0],
    [0, 0, 1],
]
mat4 = [
    [1, 0, l2],
    [0, 1, 0],
    [0, 0, 1],
]
mat5 = [
    [cos_t3, -sin_t3, 0],
    [sin_t3, cos_t3, 0],
    [0, 0, 1],
]
mat6 = [
    [1, 0, l3],
    [0, 1, 0],
    [0, 0, 1],
]

def matrix_multiply(a, b):


result1 = matrix_multiply(mat1, mat2)
result2 = matrix_multiply(result1, mat3)
result3 = matrix_multiply(result2, mat4)
result4 = matrix_multiply(result3, mat5)
final_result = matrix_multiply(result4, mat6)


x = final_result[0][2]
y = final_result[1][2]
print(float("Koordinat titik akhir ujung kaki (x, y): ({x}, {y})"))


