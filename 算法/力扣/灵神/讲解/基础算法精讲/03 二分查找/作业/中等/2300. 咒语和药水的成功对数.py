# 第一段是我自己写的二分查找做法，时间复杂度只击败了21.80%。
# 而且我还不知道为什么我一开始写target = success // spell答案就是错的，而写成target = sucess / spell就对了。

from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = [0] * len(spells)
        potions.sort() 
        for i, spell in enumerate(spells):
            target = success / spell
            left = 0 
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] += len(potions) - left 
        return pairs 
 
# 第二段是灵神 排序 + 二分查找 的 使用浮点数的代码。  
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions) 
        return [m - bisect_left(potions, success / x) for x in spells]
    
# 第三段是灵神 排序 + 二分查找 的 不适用浮点数的代码。

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        success -= 1
        return [m - bisect_right(potions, success // x) for x in spells]
    
# 还有方法二 计数 + 值域前缀和 写法，但是今天先不看这部分题解，等我把前缀和那道题做完之后再来写方法二的代码。
# 2025.11.07 13:14