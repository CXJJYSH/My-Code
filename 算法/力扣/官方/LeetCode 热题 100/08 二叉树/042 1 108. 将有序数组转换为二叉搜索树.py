# Definition for a binary tree node.

from typing import List, Optional

# 有切片写法 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None 
        
        m = len(nums) // 2
        
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])
        
        return TreeNode(nums[m], left, right) 
    
# 时间复杂度O(n * log n)，一共O(log n)层，每一层切片时间复杂度为O(n)。 
# 空间复杂度O(n)，切片复制要O(n)空间复杂度。 

# 2026.05.01 23:15 

# 没切片写法 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(left, right):
            if left == right:
                return None 
        
            m = (left + right) // 2
        
            return TreeNode(nums[m], dfs(left, m), dfs(m + 1, right)) 
        
        return dfs(0, len(nums)) 
    
# 时间复杂度O(n) 
# 空间复杂度O(log n) 

# 2026.05.01 23:18 