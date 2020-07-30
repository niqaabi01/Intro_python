#basic vector calculations using short functions 
# Saaniah Blankenberg
# Date:2020/06/18

import numpy as np
from numpy import array

a = list(map(int, input("Enter Vector A: ").split()))
b = list(map(int, input("Enter Vector B: ").split()))
a = array(a)
b = array(b)
c = a + b
print("A+B =", list(c))
# multipying each character by it's corresponding character
d = a@b
print("A.B =", d)
# for norm
print("|A| =", np.linalg.norm(a).round(2))
print("|B| =", np.linalg.norm(b).round(2))
