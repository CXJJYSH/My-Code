from typing import List

# 2025.12.04 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n 
        on_path = [False] * n 
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 
            for j in range(n):
                if not on_path[j]:
                    path[i] = nums[j]   
                    on_path[j] = True 
                    dfs(i + 1)
                    on_path[j] = False 
        dfs(0)
        return ans 
    
# 2026.05.13 12:14 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        path = [0] * n 
        on_path = [False] * n 
        ans = []

        def dfs(i):
            if i == n:
                ans.append(path.copy()) 
                return 
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j] 
                    on_path[j] = True 
                    dfs(i + 1)
                    on_path[j] = False 

        dfs(0) 
        return ans 
    
# 长度完整的时候就复制进答案。 
# 当前递归之后那些元素在for循环中依次在下一位置出现，然后各自对应相应的递归，所以不会出错，也能完整排列完。 
    
# 时间复杂度O(n * n!)，其中 n 为 nums 的长度。视频中提到，搜索树中的节点个数低于 3⋅n!。实际上，精确值为 ⌊e⋅n!⌋，其中 e=2.718⋯ 为自然常数。有 O(n!) 个叶节点，每个叶节点花费 O(n) 的时间复制 path 数组，因此时间复杂度为 O(n⋅n!)。 
# 空间复杂度O(n)，返回值的空间不计入。 

# 20026.05.13 12:20 

# 2026.05.13 12:36 