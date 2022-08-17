class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        self.num = n
        self.start = start
        
        num_list = [(self.start + 2 * i) for i in range(self.num )]
        print(num_list)
        l = len(num_list)
        result = num_list[0]
        for i in range(1, l):
            result = result ^ num_list[i]
        return result
    
x=Solution()
x.xorOperation(n = 4, start = 3)