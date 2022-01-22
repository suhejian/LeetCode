class Solution:
    def removePalindromeSub(self, s: str) -> int:
        start, end = 0, len(s) - 1
        isPalindrome = True
        while start < end:
            if s[start] != s[end]:
                isPalindrome = False
                break
            start += 1
            end -= 1
        
        if isPalindrome:
            return 1
        else:
            return 2
