from typing import List

# 方法一：从答案的角度————正确答案由哪几个构成。

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, t):
            d = k - len(path)
            
            if t < 0 or t > ((i + i - d + 1) * d) // 2:
                return 
            # 少了上面这一句就直接错。 
            # 原因应该是在t < 0的时候没有返回，而是加入答案，导致数字之和大于所要的总和；
            # t 大于之后所有个数的最大值之和时也没有返回，依旧加入答案，导致数字之和小于所要的总和的数组也加入了答案。

            if len(path) == k:
                ans.append(path.copy())
                # 而这里本应该判断t是否等于0，之后此时t还等于0时才能加入答案。
                # 然而d = 0时上面第二个式子结果也等于0，正确答案不会被剔除，上面的判断语句只剔除t < 0和t > 0的情况。
                # 所以能到达边界条件的情况必有t == 0，所以不用进行判断。
                return 
            # 边界条件

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()
            # 非边界条件

        dfs(9, n)

        return ans 
    
# 时间复杂度O(k * C(9, k)) 
# 空间复杂度O(k) 

# 中等 

# 2025.12.03 14:11 

# 方法二：从输入的角度————选或不选

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(i, t):
            d = k - len(path)
            
            if t < 0 or t > ((i + i - d + 1) * d) // 2:
                return 
            
            if len(path) == k:
                ans.append(path.copy())
                return 
            
            # 不选 
            if i > d: 
                # 这里不进行判断就错了，我现在还没找到保证正确的解释， 
                # 只知道这一句的作用是表示剩余数字够的时候可以不选、剩余数字刚好或不够的时候一定要选。 
                # 然后判断这里可以不选，再进行不选操作。 
                dfs(i - 1, t) # 注意这里是倒序枚举，所以是i - 1。 

            # 选
            path.append(i)
            dfs(i - 1, t - i) # 倒序枚举，是i - 1。 
            path.pop()
        
        dfs(9, n)
        
        return ans 
    
# 时间复杂度O(k * C(9, k)) 
# 空间复杂度O(k) 

# 中等 

# 2025.12.03 14:39 