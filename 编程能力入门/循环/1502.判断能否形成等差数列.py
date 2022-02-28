class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        dis = sorted_arr[1] - sorted_arr[0]
        for i in range(1, len(arr)):
            if sorted_arr[i] - sorted_arr[i-1] != dis:
                return False
        return True