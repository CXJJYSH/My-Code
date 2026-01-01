# 我的写法 

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_b = 0
        num_b = 0
        
        for i, x in enumerate(blocks):
            left = i - k + 1
            
            if x == "B":
                num_b += 1
            
            if i < k - 1:
                continue
            
            max_b = max(max_b, num_b)
            
            if blocks[left] == "B":
                num_b -= 1
        
        return k - max_b 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.01 17:01 

# 灵神周赛视频讲解里的写法 

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = cnt_w = blocks[:k].count("W")
        # 用方法直接统计最前面的长度为k的字符串中W的数量。 
        
        for in_, out in zip(blocks[k:], blocks): 
            # 这里用zip内置函数，将后续需要进入的元素、和需要弹出的元素进行对齐，返回一个元素是元组的迭代器，再用for循环迭代。 
            
            cnt_w += + (in_ == "W") - (out == "W") # 这里的括号不能删除，因为 - 比 == 优先级更高，删除了括号会先计算"W" - out，引起报错。 
            # 这里将“入”和“出”的步骤直接融合到同一个步骤里了，很巧妙。 
            # 将判断相不相等的布尔值结果转化成数字。 
            
            ans = min(ans, cnt_w)
            # 然后更新W的最小数量。 
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.01 17:40 