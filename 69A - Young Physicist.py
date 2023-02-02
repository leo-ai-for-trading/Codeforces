import sys
from itertools import permutations
from collections import Counter
import math
M = 1000000007

sx,sy,sz = 0,0,0
for _ in range(int(sys.stdin.readline())):
    x,y,z = map(int,sys.stdin.readline().split())
    sx += x
    sy += y
    sz += z
if sx == 0 and sy == 0 and sz == 0: 
    print("YES")
else:print("NO")
