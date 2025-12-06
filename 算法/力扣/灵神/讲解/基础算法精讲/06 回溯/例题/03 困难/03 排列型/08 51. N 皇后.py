from typing import List

# 方法一：直接枚举每一行的皇后应该在哪一列里。 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [] 
        col = [0] * n 
        
        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R - C: # 利用了主副对角线数学性质。 
                    return False 
            return True 
        
        def dfs(r, s):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col]) 
                # 这里[]必须包含整个语句。否则就错了。详情见https://chatgpt.com/c/6932843d-689c-8322-94c8-e00134dfc6f3。 
                return 
            
            for c in s:
                if valid(r, c):
                    col[r] = c 
                    dfs(r + 1, s - {c})
                    # 这里又为什么不需要恢复现场？ 
        
        dfs(0, set(range(n))) # 可以直接生成一个从0到n - 1的集合。 

        return ans 

# 粗略看为枚举全排列。 

# 时间复杂度O((n ^ 2) * n!) 
# 空间复杂度O(n) (col) 

# 困难 

# 2025.12.05 15:23 

# 方法一的另一种写法。 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [] 
        col = [0] * n 
        
        # def valid(r, c):
        #     for R in range(r):
        #         C = col[R]
        #         if r + c == R + C or r - c == R - C:
        #             return False 
        #     return True 
        
        # 即不另外定义函数的写法。 

        def dfs(r, s):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) ]for c in col)
                return 
            for c in s:
                if all(R + col[R] != r + c or R - col[R] != r - c for R in range(r)): # 在这里改。 
                    col[r] = c 
                    dfs(r + 1, s - {c})
                    # 还是不知道为什么这里又不需要恢复现场了。 

        dfs(0, set(range(n)))

        return ans 
    
# 时间复杂度O((n ^ 2) * n!)
# 空间复杂度O(n)

# 困难 

# 2025.12.05 15:32 

# 方法二：用布尔数组记录当前列是否有皇后。 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [] 
        col = [0] * n 

        on_path = [False] * n 
        
        m = 2 * n + 1
        diag1 = [False] * m 
        diag2 = [False] * m 
        
        def dfs(r):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return 
            
            for c in range(n):
                if not on_path[c] and not diag1[r + c] and not diag2[r - c]: 
                    # 这种方法把这里本来会出现的for循环优化掉了，使这段循环的时间复杂度从O(n ^ 2)降低到O(n)。 
                    col[r] = c 
                    on_path[c] = diag1[r + c] = diag2[r - c] = True 
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False 
                    # 这里又需要恢复现场了，但是我还是不知道究竟是为什么。 

        dfs(0)

        return ans 
    
# 时间复杂度O(n * n!) 
# 空间复杂度O(n) 

# 中等 

# 2025.12.05 16:13 

# 我现在知道为什么要恢复现场了。自己想出来的。 
# 宏观来看，最外层循环遍历n次，遍历第一次时就能找到至少一个解，
# 在找到一个解之后，如果不讲选的状态重置的话，
# 之后的任何一种情况都会判断出“该元素已选，不能再选”的情况，导致得不出正确答案。

# 而具体来看，可以举还剩两个元素未选的回溯情况，
# 这时肯定有对应的回溯二叉树，假定两个元素分别为1和2，
# 如果先选1
# 之后肯定还要回退到还剩两元素未选的情况，即从先选1的情况换成了先选2，
# 如果不恢复现场，此时1是已选状态，
# 选完2再想选1时，发现1已经是已选状态了，
# 这样就选不了最后一个1这个元素，导致得不出正确答案。

# 综上，依靠同一套状态保存数据的方法在修改完之后都一定要恢复现场。 

# 如果之后这个总结出现不适用的情况，再去灵神视频下留言提问。 
# https://www.bilibili.com/video/BV1mY411D7f6/?vd_source=72e41d7969e9dc71609c47e6fe7c343e&spm_id_from=333.788.videopod.sections  

# 2025.12.05 16:30 