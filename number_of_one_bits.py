class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = list()
        while(n >=1):
            bin_num.append(n % 2)
            n = n // 2
        one = bin_num.count(1)
        return one



    