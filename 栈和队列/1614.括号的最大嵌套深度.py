class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(c)
                depth = max(depth, len(stack))
            elif c == ')':
                stack.pop(-1)

        return depth