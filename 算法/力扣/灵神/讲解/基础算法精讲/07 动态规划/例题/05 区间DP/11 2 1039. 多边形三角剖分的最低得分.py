from cmath import inf
from functools import cache
from typing import List

# 记忆化搜索写法 

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @cache
        
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = inf 
            
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
                # 这里的状态转移方程的原理想出来还是有点讲究的。 
                # 灵神将多边形转化成了从起点顺时针到终点，然后从终点到起点的性质。 
                # 这样区间DP的头和尾就确定了。 
                # 再直接将起点和终点之间的线段看作三角形的边，剩下的只有遍历剩下的顶点当作这个三角形的最后一个顶点即可。 
                # 确定了一个三角形之后，多边形还剩两块区域，这两块区域的结果就交给递归。 
                # 还要初始化边界条件，当区间头尾相邻的时候，不可能构成三角形，这时候返回 值 0。 
                    
            return res 
        
        return dfs(0, n - 1) 

# 因为总状态数O(n ^ 2)，每个状态需要for循环的O(n)时间复杂度来计算结果，所以 
# 时间复杂度O(n ^ 3) 
# 空间复杂度O(n ^ 2) 

# 2025.12.19 18:41 

# 递推写法 

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        f = [[0] * n for _ in range(n)]
        
        for i in range(n - 3, -1, -1):
            # 因为要从比i大的k转移到i，要先计算k的情况，所以i要倒序遍历。 
            # 真正透彻还要看 10 2 516. 最长回文子序列 的解释。 

            # 边界条件是i + 1 == j的时候，但是这里直接跳过j == i + 1的情况，而j == i + 1的情况在函数的第二行就已经初始化好了。 
            for j in range(i + 2, n):
                # 因为要从比j小的k转移到j，要先计算k的情况，所以j要正序遍历。
                # 真正透彻还要看 10 2 516. 最长回文子序列 的解释。 

                res = inf 
                
                for k in range(i + 1, j):
                    res = min(res, f[i][k] + f[k][j] + values[i] * values[j] * values[k])
                
                f[i][j] = res
                # 在每一个状态的最后都要保存当前状态的值。 
                 
        return f[0][n - 1] 
    
# 时间复杂度O(n ^ 3) 
# 空间复杂度O(n ^ 2) 

# 2025.12.19 18:54 

# 暂时没有空间优化写法，没有找到空间优化写法，灵神的题解也没有空间优化写法，这道题的空间优化写法可能之后才会补充吧。 

# 2025.12.19 18:58 

# 2025.12.19 19:00 