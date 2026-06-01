from functools import reduce
from operator import xor
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums) 
    
# xor代表异或操作，先取nums的前两个元素进行异或，然后将结果传递给下一个元素再进行异或，最后返回最后的结果。 
# 两个相同元素异或是0，0和另一个不同的元素异或是另一个元素。 
# 就算只出现一次的元素是0也能得到正确答案，因为另一个异或的结果是0，和0异或的话还是0。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.01 17:44 