from typing import List

# 方法一：从答案的角度————枚举每一个位置应该选什么数。 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n # 也可以初始化为不定长path = []，但是不定长就要恢复现场。 
        
        def dfs(i, s):
            if i == n:
                ans.append(path.copy())
                return 
            # 边界条件 

            for x in s:
                path[i] = x
                dfs(i + 1, s - {x})
            # 非边界条件
            
        dfs(0, set(nums)) # 用set()将nums转化为集合。 

        return ans 
    
# 时间复杂度O(n * n!) 
# 节点个数粗略计算是 常数 * n! ，精确计算是 e * n! 再下取整。

# 空间复杂度O(n)

# 中等 

# 2025.12.04 16:23 

# 方法二：用布尔数组记录————用数组记录每个元素的选取状态。 
# 灵神说这是一种更通用的写法。 
# 我没看懂灵神说把“哈希表改成布尔数组”的意思是什么，哪里有对哈希表的修改？ 

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
                    # 这里因为是对每个元素的选取状态进行修改，不同分支的所有元素的选取状态不都一样， 
                    # 所以需要恢复现场，防止对之后的递归造成错误影响。 

        dfs(0)
        return ans 
    
# 时间复杂度O(n * n!) 
# 空间复杂度O(n) 

# 中等 

# 2025.12.04 20:18 

# 用path = []的话就是用append和pop修改和恢复一下现场即可。 