from typing import List

# 2025.10.16 第一遍写的代码 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #第一段代码是我先自己写的，先出现了索引超出范围的报错，然后是测试用例2只要返回1个元素我却返回了3个元素。然后思索了一番之后没调试出正确结果，就去看灵神的题解了。
        #问题在于我枚举第一个和第二个元素的时候没有对“下一个元素等于上一个元素”这种情况进行优化，枚举第一个元素时少了一个优化，在用例2中就多了一个元素；枚举第二个元素时少了一个优化，在用例2中就又多了一个元素。所以结果比正确答案多了两个元素。现在已经修正了。最后击败了70%左右。
        #但是我的最终写法还是少了最正宗的剪枝优化，即枚举时的极端情况处理。灵神的题解就完善了这个问题。
        #而且灵神最里层代码还比我少了两段冗余的优化，最后记录结果的时候也比我多考虑了双指针相遇问题。
        #修改之后提升到了80%左右 ~ 90%多的击败率。
        '''
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue 
            for j in range(i + 1, n - 2):
                x = nums[i]
                y = nums[j]
                left = j + 1
                right = n - 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break
                if x + y + nums[-1] + nums[-2] < target:
                    continue 
                while left < right:
                    if x + y + nums[left] + nums[right] < target:
                        left += 1
                    elif x + y + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        ans.append([x, y, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
        return ans 
        '''
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue 
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break 
            if x + nums[-1] + nums[-2] + nums[-3] < target:
                continue 
            for j in range(i + 1, n - 2):
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:
                    continue 
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break 
                if x + y + nums[-1] + nums[-2] < target:
                    continue 
                left = j + 1
                right = n - 1
                while left < right:
                    s = x + y + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([x, y, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans 

# 2026.03.24 第二次做的代码 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        ans = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue 
            # 这里也是要至少记一次。 
            # 直接跳过那么多元素的话可能会漏掉相同元素组成的四元组。 
        
            tar = target - nums[i]
            
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                # 应该时当前j如果能记入答案的话还是要记一次的。 
                # 我的写法可能会漏掉相同元素组成的四元组。 
                # 我的 if j < len(nums) - 1 and nums[j] == nums[j + 1]: continue 的写法应该也没有一次性跳过所有重复元素。 
            
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[j] + nums[left] + nums[right]
            
                    if s == tar: 
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
            
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
            
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
            
                    elif s > tar: 
                        right -= 1
            
                    else:
                        left += 1
        
        return ans 
    
# 时间复杂度O(n ^ 3) 
# 空间复杂度O(1) 

# 2025.03.24 23:59 