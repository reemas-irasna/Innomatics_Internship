class Solution:
    def findNumbers(self, nums) -> int:
        self.number = nums
        list_of_digit = []
        for i in self.number:
            i=str(i)
            list_of_digit.append(len(i))
        count=0
        for i in list_of_digit:
            if i%2 == 0:
                count+=1
        return count


x = Solution()
x.findNumbers([555,901,482,1771])