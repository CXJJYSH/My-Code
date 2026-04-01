from typing import List

# 这道题又没看到灵神的题解，看的是一个叫“灵茶山土地”的人的题解。 

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        cur = 0
        ans = 0
        while left <= right:
            # 有能量就追求加分 
            if power >= tokens[left]:
                power -= tokens[left]
                cur += 1
                left += 1
            # 能量不够但有分，就尝试换能量换更多分 
            elif power < tokens[left] and cur:
                # 但是这里要先把当前分数存下来，防止后面cur减小后没机会再增大了。 
                # 因为有可能这个情况执行完后没有元素可以执行了，就白白少了一分。 
                ans = max(ans, cur)
                power += tokens[right]
                cur -= 1
                right -= 1
            # 既没能量又没分数就直接跳出while循环。 
            else:
                break 
        
        # 有可能一次减分得到的能量够前面进行多次加分，所以cur有可能比之前存的ans更大，所以返回的时候还要先取一个max才能得到正确答案。 
        return max(ans, cur)
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.01 11:33 