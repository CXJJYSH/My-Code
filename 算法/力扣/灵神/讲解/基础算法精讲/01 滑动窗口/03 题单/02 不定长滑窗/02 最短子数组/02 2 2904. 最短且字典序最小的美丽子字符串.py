# 枚举的方法 

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        # 先判断是否有答案需要的"1"的个数，如果没有直接返回空串。 

        for size in range(k, len(s) + 1): # 这里的时间复杂度为O(n)。 
            # size表示子串长度，能取到len(s)，所以range中的返回要写到len(s) + 1。 

            ans = ""
            # 用ans表示该返回的答案。 

            for i in range(size, len(s) + 1): # 这里的时间复杂度也是O(n)。 
                # i最大取到len(s)。 

                t = s[i - size : i]
                # 这样就表示长度为size的子串。 
                # 子串末尾能到下标len(s) - 1，所以切片范围要写到i。 
                
                if (ans == "" or t < ans) and t.count("1") == k:
                    # Python能直接比较字符串字典序的大小，即 t < ans，但是要花费O(n)时间。 
                    # t < ans的比较时间复杂度O(n)，t.count("i")时间复杂度O(n)。
                    ans = t
            
            if ans:
                return ans 
            # 这里必须在外层for循环内return，因为外层for循环是在逐渐扩大子串长度找符合条件的答案， 
            # 如果在外层for循环内一结束内层for循环就直接return，就能保证返回的是长度最小、且满足题目条件的子串，这样才能得到正确答案。
            # 如果在外层for循环外return，就会在比较字典序大小 t < ans 时出现问题， 
            # 可能在更长的size里，找到了一个有k个"1"的t，第一个不同字符刚好是t的更小，此时就会把ans更新成更长的子串，这样就会返回错误答案。 

# 时间复杂度为三个O(n)的嵌套叠加，为O(n ^ 3)。 
# 空间复杂度O(n)，字符串切片需要O(n)空间，Go语言除外。 

# 2026.01.07 00:42 

# 滑动窗口写法 

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        ans = ""
        left = 0
        cnt1 = 0
        
        for right, c in enumerate(s):
            cnt1 += int(c) # 只有0和1元素的计数时可以直接将元素转换成整数进行加减。 
            
            while cnt1 > k or s[left] == "0": # "1"的个数大于k 或 左端点元素是"0"时都可以向右缩短子串。 
                cnt1 -= int(s[left]) # 只有0和1元素的计数时可以直接将元素转换成整数进行加减。 
                left += 1
            
            if cnt1 == k: # "1"的个数符合题意时 
                t = s[left:right + 1] # 切片出可能是答案的子串。这里切片也要O(n)的时间。 
                if ans == "" or len(t) < len(ans) or (len(t) == len(ans) and t < ans): # 三个条件判断，后面两个相当于双关键字排序。 
                    ans = t # 如果符合条件，即可更新答案。 
        
        return ans 
        # 因为滑动窗口是一直向更小的答案更新的，所以可以退出for循环后返回最后保存下来的结果，此时一定是最短的子串。 

# 如果光看外层for循环和while循环，时间复杂度只有O(n)，但是后面的切片和字典序大小比较都要一次单独的O(n)时间，所以综合起来 
# 时间复杂度为O(n ^ 2) 
# 空间复杂度O(n)，字符串切片需要O(n)空间，Go语言除外。 

# 2026.01.07 01:10 

# 滑动窗口写法还可以优化，优化为将ans初始化成s，可以省去后面的一个 ans == "" 判断步骤。 
# 因为必有答案、又没有更短的符合条件的答案时，s本身就是答案，此时也没有一样长但字典序更小的子串。 

# 优化写法 

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        ans = s
        left = 0
        cnt1 = 0
        
        for right, c in enumerate(s):
            cnt1 += int(c)
            
            while cnt1 > k or s[left] == "0":
                cnt1 -= int(s[left])
                left += 1
            
            if cnt1 == k:
                t = s[left:right + 1]
                if len(t) < len(ans) or (len(t) == len(ans) and t < ans):
                    ans = t
        
        return ans 
    
# 这还是灵神直播讲题的时候一个观众提出来的，灵神一开始都没想到，灵神试了一下之后说这个优化写得好。 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n) 

# 2026.01.07 01:15 