class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []
        if len(s) % 2 == 1:
            return False

        for i in range(len(s)):
            if s[i] in hashmap:
                if len(stack) == 0 or stack[-1] != hashmap[s[i]]:
                    # 不匹配
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        
        return True if len(stack) == 0 else False

