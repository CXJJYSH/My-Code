from typing import List

# 灵神的写法 

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        # 看了灵神的题解，从这种简单的写法中学到了严谨简洁的逻辑思维，即这道题中先装水再立即浇水，而且判断语句只需要判断要不要装水，而不需要进行指针移动。要分清每一段代码负责什么功能。
        
        ans = 0
        n = len(plants)
        a, b = capacityA, capacityB
        i, j = 0, n - 1
        while i < j:
            if a < plants[i]:
                a = capacityA
                ans += 1
            a -= plants[i]
            i += 1
            if b < plants[j]:
                b = capacityB
                ans += 1
            b -= plants[j]
            j -= 1
        if i ==j and max(a, b) < plants[i]:
            ans += 1
        return ans 
    
# 我的写法 

# 花了19分钟 2026.03.15 18:45 - 19:07  

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        
        left = 0
        right = len(plants) - 1
        
        waterA = capacityA
        waterB = capacityB
        
        while left < right: 
            # while循环只考虑 left < right 的情况，left == right 和 left > right 的情况考虑。 
            # left < right 的情况单独判断更好。 
            # left > right 的情况则不用判断。 

            # 先对左指针进行判断。 

        
            if waterA >= plants[left]:
                waterA -= plants[left]
                left += 1
            else:
                ans += 1
                waterA = capacityA - plants[left]
                left += 1
        
            # 再对右指针进行判断。 

            if waterB >= plants[right]:
                waterB -= plants[right]
                right -= 1
            else:
                ans += 1
                waterB = capacityB - plants[right]
                right -= 1
        
        # 在循环外对 left < right 的情况单独判断。 

        if left == right:
                if waterA >= waterB:
                    if waterA < plants[left]:
                        ans += 1
                else:
                    if waterB < plants[right]:
                        ans += 1
        
        # 最后返回答案。 

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.15 19:10 

# 刚才Git同步又出问题了，现在再试试。 

# 2026.03.15 19:15 