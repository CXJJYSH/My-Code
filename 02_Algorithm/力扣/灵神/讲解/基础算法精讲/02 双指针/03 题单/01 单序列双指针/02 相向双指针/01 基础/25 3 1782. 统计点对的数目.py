from typing import Counter, List

# 灵神的写法 
# 困难题，自己没想出来 

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # 本题的目的是统计满足条件的边的数目 

        # 这里是在为判断是否满足条件做准备，统计该边节点相连的边的数目 
        deg = [0] * (n + 1) # 空间复杂度O(n) 
        for x, y in edges:
            deg[x] += 1
            deg[y] += 1
        
        # 统计每条边的出现次数 
        cnt_e = Counter(tuple(sorted(e)) for e in edges) # 空间复杂度O(m)，m = len(edges) 


        ans = [0] * len(queries)

        # 排序为了双指针查找 
        # 时间复杂度O(n log n) 
        sorted_deg = sorted(deg)
        
        for j, q in enumerate(queries): # 时间复杂度O(q)，q = len(queries) 
            # j对应答案的索引，q代表当前queries中的元素 
            
            # 时间复杂度O(n) 
            left = 1
            right = n
            while left < right:
                if sorted_deg[left] + sorted_deg[right] <= q:
                    left += 1
                else:
                    ans[j] += right - left 
                    right -= 1

            # 时间复杂度O(m) 
            # 这里是遍历字典的 键 和 值 。 
            # 即边和对应的数目 
            # 重复统计的相邻边数目就是该边的数目 
            # 减掉以后如果小于或等于当前queries中的元素，则将答案中符合条件的边数减一。 
            for (x, y), c in cnt_e.items():
                if deg[x] + deg[y] > q and deg[x] + deg[y] - c <= q: # 这里还可以写成 q < deg[x] + deg[y] <= q + c 。 
                    ans[j] -= 1

        return ans 
    
# 时间复杂度O(n log n + q * (n + m)) 
# 空间复杂度O(n + m) 

# 2026.04.08 12:01 