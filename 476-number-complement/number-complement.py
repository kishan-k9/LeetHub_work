class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (2 ** int(log(num, 2) + 1) - 1)