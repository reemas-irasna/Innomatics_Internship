class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        self.n = n
        product_of_num =1
        sum_of_num =0
        for i in str(self.n):
            product_of_num *= int(i)
            sum_of_num += int(i)
        return(product_of_num - sum_of_num)

x=Solution()
x.subtractProductAndSum(234)