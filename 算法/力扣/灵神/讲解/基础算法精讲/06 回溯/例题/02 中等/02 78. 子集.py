from typing import List

# 方法一：站在“输入”的角度思考————对已给数组的每一个元素，要么选，要么不选。 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = [] # 定义全局变量。
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy()) 
                # 这里用copy()的原因是整个递归是不断地对全局变量path修改， 
                # 如果不用copy()，当所有递归都结束时，每个递归产生的ans都因为对应着path而是相同的结果， 
                # 而用了copy()，就能保证每一个递归都返回当前递归出的答案、且与其它答案不同， 
                # 这样才达成了题目的目的。 

                return 
                # 到达边界条件时return， 
                # 因为最后的答案有其它专门的形式保存着用来return， 
                # 所以这里的return只用简单的一个return就可以了， 
                # 一个单独的return才正确。 
            
            dfs(i + 1)

            path.append(nums[i]) # 修改 
            dfs(i + 1)
            path.pop() # 回退 

            # 上面的“不选”和“选”的代码顺序是可以调换的，因为每一个代码块的逻辑都正确无误。

        dfs(0)
        
        return ans 
    
# 时间复杂度为O(n * (2 ^ n))， 
# 因为每一步2种选择，总流程为O(2 ^ n)， 
# 每一个递归流程最后一步的copy()花费O(n)时间， 
# 所以整体的时间复杂度为O(n * (2 ^ n))。 

# 空间复杂度为全选情况下path占用的额外空间O(n)。

# 中等 

# 2025.12.01 18:03 

# 方法二：站在“答案”的角度思考————每次要么不选，要么选比当前元素大的数（由于集合的性质）。 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            ans.append(path.copy())
            # 每进入一个递归，当前状态就是一个答案。 

            if i == n:
                return
            # 边界条件。 
             
            for j in range(i, n): 
                # 因为这个循环中j最多到n - 1，之后递归j + 1会因为j + 1 = n不在循环范围里而结束， 
                # 和判断if i = j + 1 == n: return的效果是一样的， 
                # 所以前面的边界条件那两行可以省略。 

                path.append(nums[j])
                dfs(j + 1)
                path.pop()
                # 依旧“修改 - 回退”。 
                # 直接套用“修改 - 回退”模板。 

            # 按照特定的顺序不重复地挑选元素。 

        dfs(0)

        return ans 
    
# 时间复杂度应该还是O(n * (2 ^ n))
# 空间复杂度应该还是O(n)

# 中等

# 2025.12.01 18:35 