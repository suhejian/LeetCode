class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(s[i].lower())
            if s[i].isdigit():
                res.append(s[i])
        start, end = 0, len(res) - 1
        while start < end:
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        return True