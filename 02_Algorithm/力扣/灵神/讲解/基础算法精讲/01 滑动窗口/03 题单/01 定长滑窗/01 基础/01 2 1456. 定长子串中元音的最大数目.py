class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # 定长滑窗

        ans = vowel = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                vowel += 1
            left = i - k + 1
            if left < 0:
                continue
            ans = max(ans, vowel)
            if ans == k:
                break
            if s[left] in "aeiou":
                vowel -= 1
        return ans 

# 2025.10.21 12:03