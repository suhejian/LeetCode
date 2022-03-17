class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numOne(num):
            res = 0
            for i in range(32):
                res += (num >> i) & 1
            return res, num
        
        arr.sort(key=numOne, reverse=False)
        return arr