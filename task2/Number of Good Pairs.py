class Solution:
    def numIdenticalPairs(self, nums) -> int:
        self.nums = nums
        l = len(self.nums)
        count = 0
        for i in range(l):
            for j in range(l):
                if self.nums[i] == self.nums[j] and i<j:
                    count+=1
        return count

x=Solution()
x.numIdenticalPairs([1,1,1,1])