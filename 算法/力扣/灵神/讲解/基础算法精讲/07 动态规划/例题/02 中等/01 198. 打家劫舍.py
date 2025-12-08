# 这一题只是入门，从记忆化搜索到递推。 

from typing import List

# 记忆化搜索 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = [-1] * n # 保存计算结果  

        # 递归搜索         
        def dfs(i):
            if i < 0:
                return 0 
            
            if cache[i] != -1:
                return cache[i] 
            
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            
            cache[i] = res 
            
            return res 
        
        return dfs(n - 1) 
    
# 递归搜索 + 保存计算结果 = 记忆化搜索 

# 动态规划时间复杂度计算公式：状态个数 × 单个状态所需要的计算时间 
# 这里状态个数是O(n)的，单个状态的计算时间是O(1)的，所以时间复杂度就是O(n)，空间复杂度也是O(n)。

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 中等 

# 2025.12.08 15:44 

# 优化（优化空间复杂度）

# 自顶向下算：记忆化搜索 
# 自底向上算：递推 

# 先将 记忆化搜索 代码改成 递推 代码 

# 递推（这里还没有优化空间复杂度）

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        f = [0] * (n + 2)
        
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + nums[i])
        
        return f[n + 1] 
    
# 优化完成 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0 
        # f0代表上上一个结果，f1代表上一个结果。 

        for i, x in enumerate(nums):
            new_f = max(f1, f0 + x) 
            f0 = f1 
            f1 = new_f 
        
        return f1 # 这里return new_f也可以，但是可能其它语言只能return f1，所以这里还是return f1比较好，以免养成不好的习惯。 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2025.12.08 16:18 