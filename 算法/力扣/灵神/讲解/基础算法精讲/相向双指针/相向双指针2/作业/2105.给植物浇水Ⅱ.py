class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        
        # 看了灵神的题解，从这种简单的写法中学到了严谨简洁的逻辑思维。
        # 即这道题中先装水再立即浇水，而且判断语句只需要判断要不要装水，而不需要进行指针移动。要明确每一段代码负责什么功能。
        
        ans = 0
        n = len(plants)
        a, b = capacityA, capacityB
        i, j = 0, n - 1
        while i < j:
            if a < plants[i]:
                a = capacityA
                ans += 1
            a -= plants[i]
            i += 1
            if b < plants[j]:
                b = capacityB
                ans += 1
            b -= plants[j]
            j -= 1
        if i ==j and max(a, b) < plants[i]:
            ans += 1
        return ans