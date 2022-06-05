class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        for num in arr:
            div, mod = divmod(num,2)
            if (div == 0 and mod == 0 and arr.count(0)>=2) or (div !=0 and mod == 0 and div in arr):
                return True
        return False