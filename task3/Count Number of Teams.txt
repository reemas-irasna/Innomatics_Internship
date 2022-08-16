class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[0, 0] for i in range(n)]
        res = 0
        for k in range(1, n):
            for j in range(0, k):
                # . j. k
                if rating[j]<rating[k]:
                    res += dp[j][0]
                    dp[k][0] += 1
                if rating[j]>rating[k]:
                    res += dp[j][1]
                    dp[k][1] += 1
        return res