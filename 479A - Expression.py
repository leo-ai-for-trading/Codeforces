import sys
from itertools import permutations
from collections import Counter
import math
M = 1000000007

a = (int(sys.stdin.readline()))
b = (int(sys.stdin.readline()))
c = (int(sys.stdin.readline()))

ans = a+b+c
ans = max(ans,(a*b*c))
ans = max(ans,((a+b)*c))
ans = max(ans,(a*(b+c)))
ans = max(ans, (a+(b*c)))
ans = max(ans, (a*b)+c)
print(ans)
