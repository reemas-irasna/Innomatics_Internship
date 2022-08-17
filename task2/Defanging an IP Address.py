class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        output =''
        for i in self.address:
            if i == '.':
                output += "[.]"
            else:
                output += i
        return output
    
x= Solution()
x.defangIPaddr("1.1.1.1")