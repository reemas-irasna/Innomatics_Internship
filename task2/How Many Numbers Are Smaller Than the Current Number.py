class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        self.nums = nums
        l = len(self.nums)
        count=0
        count_of_num =[]
        for i in range(l):
            count=0
            for j in range(l):
                if self.nums[j] !=self.nums[i] and self.nums[i] > self.nums[j]:
                    count+=1
            count_of_num.append(count)
        
        return(count_of_num)

x=Solution()
x.smallerNumbersThanCurrent([8,1,2,2,3])