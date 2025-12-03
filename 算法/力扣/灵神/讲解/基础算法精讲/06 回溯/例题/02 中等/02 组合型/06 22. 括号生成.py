from typing import List

# 方法一：从输入的角度————选左括号还是选右括号。 

# 需要恢复现场的方法。 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [] # 因为初始化path长度不确定、之后会存在逆向现象，所以之后需要恢复现场、append之后要用pop。 

        def dfs(i, open):
            if i == m: # 最后递归到dfs(i + 1)的时候就会有i + 1 == m。 
                ans.append("".join(path))
                return 
            
            # 选左括号。 
            if open < n:
                path.append("(")
                dfs(i + 1, open + 1)
                path.pop()

            # 选右括号。 
            if i - open < open:
                path.append(")")
                dfs(i + 1, open)
                path.pop()

        dfs(0, 0)

        return ans 
    
# 不需要恢复现场的方法。 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [""] * m # 因为这的path是定长所以不需要恢复现场。 

        def dfs(i, open):
            if i == m:
                ans.append("".join(path))
                return 
            
            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)
                
            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)
                
        dfs(0, 0)

        return ans 
    
# 时间复杂度O(n * C(2n, n))，可以看成是2n个位置中选n个位置放左括号，剩下的n个位置自然就是右括号了。 
# 灵神说左右括号之间是有约束的，所以实际递归次数没有那么多。原理要去了解卡特兰数。 
# 灵神题解卡特兰数时间复杂度分析结果：https://mubu.com/app/edit/recent/3Oqp73YCBw3#E8UZu6G1YD。 

# 空间复杂度O(n) 

# 中等 

# 2025.12.03 15:34 

# 方法二：从答案的角度————枚举下一个左括号的位置。 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = [] # path保存的是左括号的索引。 

        # 目前填了 i 个括号。 
        # balance = 这 i 个括号中的左括号个数 - 右括号个数。 
        def dfs(i, balance):
            
            if len(path) == n: # 这里意思是填满了n个左括号。实际上是保留了所有左括号的下标，这里是要用索引对相应位置进项修改。 
                
                s = [")"] * (n * 2)
                
                for j in path:
                    s[j] = "(" # 括号个数为什么和索引就能对上啊。 
                
                ans.append("".join(s))
                
                return 
            
            for right in range(balance + 1): # balance + 1我看了题解能理解。 
                
                path.append(i + right) # 这里的数量关系不太清楚要不要加减。 
                dfs(i + right + 1, balance - right + 1) # 这里也不太清楚为什么又要 + 1 了。 
                path.pop()
        
        dfs(0, 0)

        return ans 
    
# 题解链接：https://leetcode.cn/problems/generate-parentheses/solutions/2071015/hui-su-bu-hui-xie-tao-lu-zai-ci-pythonja-wcdw/。 

# 时间复杂度O(n * C(2n, n)) 
# 空间复杂度O(n) 

# 中等

# 2025.12.03 16:25 