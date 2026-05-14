from typing import List

# 选或不选 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return 
            
            if i == len(candidates) or left < 0:
                return 

            dfs(i + 1, left) 

            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        dfs(0, target)
        return ans 
    
# 时间复杂度O(n log n + 常数) 
# 空间复杂度O(target) 
    
# 剪枝优化写法 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return 
            
            if i == len(candidates) or left < candidates[i]:
                return 

            dfs(i + 1, left) 

            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        dfs(0, target)
        return ans 
    
# 速度一下从百分之四十多升到了百分之九十多。 
    
# 时间复杂度O(n log n + 常数) 
# 空间复杂度O(target) 

# 2026.05.14 12:45 

# 枚举选哪个 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return 

            for j in range(i, len(candidates)):
                if candidates[j] > left:
                    break 

                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()

        dfs(0, target)
        return ans 
    
# 复杂度如方法一 

# 完全背包预处理 + 可行性剪枝 

# 这方法我还不会，也还没看，之后有机会去看。 

# https://leetcode.cn/problems/combination-sum/solutions/2747858/liang-chong-fang-fa-xuan-huo-bu-xuan-mei-mhf9/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.14 12:53 