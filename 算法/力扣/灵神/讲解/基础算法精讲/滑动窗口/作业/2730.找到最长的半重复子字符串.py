class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        # 卧槽，完全靠自己写出来的第一道中等题，太牛逼了，卧槽，爽！

        # 下面是我的写法。
        
        ans = 0
        cnt = 0
        left = 0
        for right, i in enumerate(s): # 这里改成for right in range(len(s)): 时间复杂度就从击败32.26%提升到80.84%了。
            if right > 0 and s[right] == s[right - 1]:
                cnt += 1
            while cnt > 1:
                if s[left] != s[left + 1]:
                    left += 1
                else:
                    cnt -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans

        # return后面的代码不会执行。

        # 下面是灵神的写法。
        # 灵神的写法时间复杂度击败了89.39%。
        # 优化应该在于没用enumerate枚举，并且range范围小了1。其它的区别就更细小，不太好判断了。

        ans = 1 # 这里一定要初始化为1，不然当len(s) == 1的时候for循环进不去会导致结果错误。
        left = 0
        cnt = 0
        for right in range(1, len(s)):
            cnt += s[right] == s[right - 1]
            if cnt > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                cnt -= 1
            ans = max(ans, right - left + 1)
        return ans