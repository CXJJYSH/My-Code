from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        
        ans = 0
        
        def dfs(x):
            nonlocal ans 
            
            x_len = 0 # 这里的x_len代表的是“以x为根节点的普通树 拥有的最长链长，这里的链长是用x节点以下 边的个数表示的”。
            
            for y in g[x]:
                y_len = dfs(y) + 1 
                # 这里的y_len其实并不是和x_len拥有相同的含义， 
                # 这里的y_len表示的其实就是“以x为根节点的普通树的当前链的链长，链长用x节点以下的边的个数表示”。 
                # 这样就要用“以y为根节点的普通树的 用边表示的 最大链长”，加上x与y连接的那条边的长度————1，才能正确表示。 
                
                if s[y] != s[x]:
                    ans = max(ans, x_len + y_len)
                    # 若符合题目条件，则将最长的两条链长加起来，更新答案，这时候还只是加上了两段边的数目。 

                    x_len = max(x_len, y_len)
                    # 若符合题目条件，则将“以x为根节点的普通树的最长链长”更新为最长链长，依旧用边的数目表示。 
            
            return x_len 
            # 最后当前节点的递归函数就返回“以当前节点为根节点的普通树的 用边的数目表示的 最长链长”。 
        
        dfs(0)
        # 最后从0开始递归，这样才能找到整棵树的答案最大值。 
        
        return ans + 1 
        # 而因为之前的ans只是表示了边的数目，想要返回点的数目就要用边的数目加一，才能得到正确答案。 
        # 这样就写完了。任何一个细节出错可能都得不到正确答案。 

# 遍历所有节点，计算时间为O(1)，没有额外空间， 所以 
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.23 00:37 

# x的邻居除了包含x的子节点，还包含x的父节点的情况的写法。 

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        
        ans = 0
        
        def dfs(x, fa): # 这里后面传入一个参数表示x的父节点。 
            nonlocal ans 
            
            x_len = 0
            
            for y in g[x]:
                if y == fa:
                    continue 
                # 如果列表中的节点y等于x的父节点，那就不计算这种情况，直接continue。 
                
                y_len = dfs(y, x) + 1
                # 这里y后面传入x，表示x是y的父节点。 

                if s[y] != s[x]:
                    ans = max(ans, x_len + y_len)
                    x_len = max(x_len, y_len)
            
            return x_len 
        
        dfs(0, -1)
        # 递归入口这里填-1，因为0表示根节点，没有父节点，用-1表示即可。 
        
        return ans + 1 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.23 00:47 