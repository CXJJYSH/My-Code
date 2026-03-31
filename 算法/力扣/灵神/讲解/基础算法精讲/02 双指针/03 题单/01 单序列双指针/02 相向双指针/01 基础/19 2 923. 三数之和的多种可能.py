from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        
        arr.sort()
        
        ans = 0
        
        n = len(arr)
        
        for i in range(len(arr)):
            j = i + 1
            k = n - 1
            while j < k:
                s = arr[i] + arr[j] + arr[k]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    if arr[j] == arr[k]:
                        # 我写代码的时候重复元素的情况想到了，但是j和k元素相同的情况我没想到。 
                        ans += (k - j + 1) * (k - j) // 2
                        # 这里的意思是j到k是连续的相同的元素，直接总数选2就是新的方案数。 
                        ans %= mod 
                        # 每次答案加了方案数之后取模，或作最后return ans % mod也行。 
                        # 这里写的话就要写成等算式。 
                        break
                        # 这里因为全是相同元素，不用再找了，就直接跳出while循环。 
                    else:
                        # 我用的是灵神的跳过重复元素写法。
                        # 循环时j可以等于k，因为可能是两组相邻的元素，j移动完毕后会指向k中的元素，之后的k循环就会达到j==k的情况。 

                        left = 1
                        j += 1
                        while j <= k and arr[j] == arr[j - 1]:
                            # j循环中循环条件不可能同时满足， 
                            # j能等于k，但是因为j和k元素组的元素不相同，不可能出现arr[j] == arr[j - 1]的情况， 
                            # 假设arr[j] == arr[j - 1]，意味着arr[k] == arr[j - 1]，然而元素组元素不一样，矛盾，所以假设不成立。 
                            # 所以这里可以写成j < k，但是下面的k循环就不行了。 
                            j += 1
                            left += 1

                        right = 1
                        k -= 1
                        while j <= k and arr[k] == arr[k + 1]:
                            k -= 1
                            right += 1

                        ans += left * right 
                        ans %= mod 
                        # 每次答案加了方案数之后取模，或作最后return ans % mod也行。 
                        # 这里写的话就要写成等算式。 
        return ans
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(1) 

# 2026.03.31 23:34 

# 2026.03.31 23:54 