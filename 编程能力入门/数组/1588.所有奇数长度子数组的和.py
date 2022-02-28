class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        lengths = list(range(1, len(arr) + 1, 2))
        total = 0
        for start in range(len(arr)):
            ends = [start + length for length in lengths if start + length <= len(arr)]
            for end in ends:
                total += sum(arr[start: end])
        return total