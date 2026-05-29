from collections import defaultdict

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        
        for right, x in enumerate(answerKey):
            cnt[x] += 1
            
            while cnt["T"] > k and cnt["F"] > k:
                out = answerKey[left]
                cnt[out] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans 
    
# 这道题最难的地方就在于将抽象的题目表述转化成我会写的滑动窗口表述，即将“最多k次操作”转换成“子字符串中最多有k个T，或者最多有k个F”。 
# 再转化成标准的维持条件的while条件表述就是“子字符串中T和F都大于k个的时候不符合题意，需要调整，直到T和F中至少有一个的个数小于或等于k”， 
# 因为只有T和F中至少有一个的个数小于或等于k时，才能保证能通过最多k次操作将子字符串变化成连续的T或F字符串。 

# 时间复杂度O(n)，准确来说最多就 2 * n 次操作，所以时间复杂度为O(n)。 
# 空间复杂度O(1) 

# 2026.01.05 23:54 