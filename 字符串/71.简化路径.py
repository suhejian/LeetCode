class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        for token in tokens:
            if token == "..":
                if stack:
                    stack.pop(-1)
            elif token and token != '.':
                stack.append(token)

        return "/" + "/".join(stack)