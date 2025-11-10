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
    
# 还有方法二 计数 + 值域后缀和 写法，但是今天先不看这部分题解，等我把前缀和那道题做完之后再来写方法二的代码。
# 2025.11.07 13:14

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        mx = max(potions)
        cnt = [0] * (mx + 1) # 初始化计数数组，包含0，0和1到mx总共有(mx + 1)个数，所以初始化数组长度为(mx + 1)。
        
        for y in potions:
            cnt[y] += 1 # 统计每种药水的出现次数
        
        # 计算 cnt 的后缀和
        for i in range(mx - 1, -1 , -1):
            cnt[i] += cnt[i + 1] 
        # 这里是从数组的倒数第二个元素开始从后往前遍历的，因为最后一个元素不用更新，只需要从倒数第二个元素开始更新。
        # 计算完毕后，cnt[i] 就是 potions 值 >= i 的药水个数
        
        for i, x in enumerate(spells):
            low = (success - 1) // x + 1
            spells[i] = cnt[low] if low <= mx else 0 
        # 这里是查找满足条件的最小元素是否在potions里，如果在(low <= mx)则返回cnt[low]，如果不在(不满足low <= mx)则返回0。
        return spells # 这是原地改变spells数组然后返回spells。且一次改变一个spells的元素不会影响最后答案的正确性。 