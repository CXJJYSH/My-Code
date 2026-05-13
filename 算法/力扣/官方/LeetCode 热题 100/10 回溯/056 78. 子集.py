from typing import List

# 2025.12.01 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            ans.append(path.copy())
            if i == n:
                return 
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans 
    
# 2026.05.13 

# 选与不选(输入的视角) 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy()) 
                return 
            
            # 不选nums[i]，下面是选nums[i]。 
            dfs(i + 1)

            # 选nums[i]。 
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            # 选与不选的顺序调换也没关系，结果是一样的。 

        dfs(0) 
        return ans 
    
# 时间复杂度O(n * (2 ** n))，其中 n 为 nums 的长度。有 2 ** n 个子集，所以搜索树有 2 ** n 个叶子，每个叶子复制 path 需要 O(n) 的时间，一共需要 O(n * (2 ** n)) 时间。 
# 空间复杂度O(n)，返回值的空间不计。 

# 2026.05.13 12:42 

# 枚举选哪个(答案的视角) 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        ans = []
        path = []

        def dfs(i):
            ans.append(path.copy()) 
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        
        dfs(0) 
        return ans 
    
# 在我看来，每个回复现场的操作是为for循环中下一个分支正确递归做的准备。 

# 时间复杂度O(n * (2 ** n)) 
# 空间复杂度O(n) 

# 2026.05.13 12:48 

# 二进制枚举

# 这是啥玩意 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):  # 枚举全集 U 的所有子集 i
            subset = [x for j, x in enumerate(nums) if i >> j & 1]
            ans.append(subset)
        return ans
    
# 没看懂，根本没看。 

# 时间复杂度O(n * (2 ** n)) 
# 空间复杂度O(1) 

# 2026.05.13 12:50 