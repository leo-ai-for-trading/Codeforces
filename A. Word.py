import sys
from itertools import permutations
from collections import Counter
import math
M = 1000000007

s = input()
l,u = 0,0
for i in s:
    if i.islower():
        l += 1
    elif i.isupper():
        u += 1
if u > l:
    print(s.upper())
else: print(s.lower())
