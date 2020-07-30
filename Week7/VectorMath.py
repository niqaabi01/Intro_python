#basic calculations using coded functions and vectors
# Saaniah Blankenberg
# Date:2020/06/18

from math import sqrt
from numpy import array
a = list(map(int, input("Enter Vector A: ").split()))
b = list(map(int, input("Enter Vector B: ").split()))
a = array(a)
b = array(b)


def add():
    A = a[0] + b[0], a[1] + b[1], a[2] + b[2]
    print(list(A))


add()


def dot():
    M = a[0] * b[0], a[1] * b[1], a[2] * b[2]
    outcome = M[0] + M[1] + M[2]
    print("A.B = ", outcome)


dot()

norm_a = sqrt((a[0] ** 2) + (a[1] ** 2) + (a[2] ** 2))
norm_b = sqrt((b[0] ** 2) + (b[1] ** 2) + (b[2] ** 2))
print("|A| = ",norm_a.__round__(2))
print("|B| = ",norm_b.__round__(2))