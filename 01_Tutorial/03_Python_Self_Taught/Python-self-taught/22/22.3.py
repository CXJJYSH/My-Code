class Solution:
    def maximumWealth(self, accounts):
        m = len(accounts)
        max_wealth = 0
        for i in range(m):
            current_wealth = 0
            n = len(accounts[i])
            for j in range(n):
                current_wealth+=accounts[i][j]
            max_wealth = max(max_wealth,current_wealth)
        return max_wealth
solution = Solution()
accounts = [[1,2,3],[3,2,1]]
print(solution.maximumWealth(accounts))
