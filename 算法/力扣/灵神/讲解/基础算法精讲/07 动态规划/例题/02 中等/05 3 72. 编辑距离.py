from functools import cache

# 记忆化搜索写法 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        @cache 
        
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            # 两个边界条件，长度都表示从0到i、j的长度。 
                        
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1) # 如果相等直接删除。
                # 这里的原理是如果末尾的两个元素相等，那么相当于这两个元素直接归类于相同的部分，不需要进行操作，可以看作直接消失， 
                # 所以不占用修改操作数。 
            else:
                return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
                # 分别是删除、插入、替换操作，等任一操作操作完了，末尾两元素才能看作是不需要进行操作的两元素，这时才可以继续递归， 
                # 而删除、插入、替换任一操作都占用一个操作数，所以在取最小值外面要加一个1。 
        
        return dfs(n - 1, m - 1) 
    
# 2025.12.12 18:35 

# 递推写法（未优化） 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        f = [[0] * (m + 1) for _ in range(n + 1)]
        
        # 下面要进行边界条件从记忆化搜索到递推的翻译。
        
        # 记忆化搜索的边界条件： 
        # i < 0，j边界是m - 1，要正确表示完整数组长度的话j需要加1 
        # 和 
        # j < 0，i边界是n - 1，要正确表示完整数组长度的话i需要加1 
        
        # 现在因为防止了负数下标所有下标都加了1，导致边界条件变为： 
        # i = 0，j边界是m，可以直接正确表示数组最大长度，
        # 和 
        # j = 0，i边界是n，可以直接正确表示数组最大长度， 
        # 所以此时的边界条件是f[0][j] = j和f[i][0] = i， 
        
        # 因为下标都加了1，
        # 所以 
        # f[0][j] = j表示为f[0] = list(range(m + 1))， 
        # f[i][0] = i表示为f[i + 1][0] = i + 1。 
        
        # （让我受到启发的弹幕：这里i和j之前是从n-1和m-1开始的，小于0时表示选完，现在都加1了，0表示选完，从n和m开始，所以当i=0(选完)时，j就是字符串t的长度） 
        
        f[0] = list(range(m + 1))
        
        for i, x in enumerate(word1):
            
            f[i + 1][0] = i + 1
            
            for j, y in enumerate(word2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] # 直接相等，不需要操作。 
                else:
                    f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
                    # 分别是删除、插入、替换操作，分析如上。 
        
        return f[n][m] 
    
# 时间复杂度O(nm) 
# 空间复杂度O(nm) 

# 2025.12.12 18:59 