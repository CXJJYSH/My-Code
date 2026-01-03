from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        # 这里采用-1进行初始化赋值才不会产生错误答案。 
        # 如果我用0初始化赋值，然后想用一个for循环进行前面的长度不足的地方的-1赋值，那样会遗漏列表末尾的-1赋值。 
        # 而且使用额外的for循环代码不够简洁优雅。 
        # 所以使用-1进行初始化是最好的写法，这也是一个因情况随机应变的小技巧。 
        
        s = 0
        
        for i, x in enumerate(nums):
            # 入 
            s += x
            
            if i < 2 * k:
                continue
            
            # 更新 
            avgs[i - k] = s // (2 * k + 1) 
            
            # 出 
            s -= nums[i - 2 * k]
        
        return avgs 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.01 16:50 