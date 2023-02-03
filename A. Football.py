import sys
from itertools import permutations
from collections import Counter
import math
M = 1000000007

s = input()
z,o = 0,0
for i in s:
    if z == 7 or o == 7:
        break
    if i == "0":
        z += 1
        o = 0
    else:
        z = 0
        o += 1
if z >= 7 or o >= 7:
    print("YES")
else: print("NO")
