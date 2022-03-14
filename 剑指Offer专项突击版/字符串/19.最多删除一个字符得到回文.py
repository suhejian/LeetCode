class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, left, right):
            # 从位置left到位置right是否为回文串
            start, end = left, right
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        # 拥有一次删除字符的机会，要么删左边的要么删右边的
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return isPalindrome(s, start, end -1) or isPalindrome(s, start+1, end)
            start += 1
            end -= 1
        return True
