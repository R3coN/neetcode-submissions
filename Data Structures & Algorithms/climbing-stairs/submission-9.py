dp = [0, 1, 2]
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return 1
        # elif n >= 2:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # for i in range(1,n+1):
        #     if i == 1:
        #         dp.append(1)
        #     elif i == 2:
        #         dp.append(2)
        #     else:
        #         if len(dp) <= i:
        #             dp.append(dp[i-1] + dp[i-2])

        while len(dp) <= n:
            dp.append(dp[-1] + dp[-2])
        return dp[n]