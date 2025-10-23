from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:

        # 其实自己最开始想出这道题的完整写法了，但是没有说服自己自己想出的写法是正确有效的。
        # 还是不能快速确定正确有效的写法，还需练习。
        # 还需积累自信。
        
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, i in enumerate(nums):
            cnt[i] += 1
            while cnt[i] > k:
                cnt[nums[left]] -= 1 # 我这里忘了left只是一个索引不是值了，犯了只写索引的错误，最后造成超出内存限制。
                left += 1
            ans = max(ans, right - left + 1)
        return ans