from cmath import inf
from functools import cache
from math import isqrt

# 递归 

@cache

def dfs(i, j):
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n) 
    
# 时间复杂度看不懂为什么是O(n * (n ** 0.5))，一共O(n * (n ** 0.5))个状态，每个状态计算的时间为O(1)。 
# 空间复杂度O(n * (n ** 0.5))。 

# 2026.05.27 14:34 

# 循环

N = 10000
f = [[0] * (N + 1) for _ in range(isqrt(N) + 1)]
f[0] = [0] + [inf] * N 

for i in range(1, len(f)):
    for j in range(N + 1):
        if j < i * i:
            f[i][j] = f[i - 1][j] 
        else:
            f[i][j] = min(f[i - 1][j], f[i][j - i * i] + 1)

class Solution:
    def numSquares(self, n: int) -> int:
        return f[isqrt(n)][n]
    
# 时间复杂度O(N * (N ** 0.5)) 
# 空间复杂度O(N * (N ** 0.5)) 

# 2026.05.27 14:40 

# 循环空间优化 

N = 10000
f = [0] + [inf] * N 

for i in range(1, isqrt(N) + 1):
    for j in range(i * i, N + 1):
        f[j] = min(f[j], f[j - i * i] + 1) 

class Solution:
    def numSquares(self, n: int) -> int:
        return f[n] 
    
# 时间复杂度O(N * (N ** 0.5)) 
# 空间复杂度O(N) 

# 2026.05.27 14:43 