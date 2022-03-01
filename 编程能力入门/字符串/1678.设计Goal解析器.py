class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while i < len(command):
            c = command[i]
            if c == 'G':
                res.append('G')
                i = i + 1
            elif c == '(':
                if command[i+1] == ')':
                    res.append('o')
                    i = i + 2
                else:
                    res.append('al')
                    i = i + 4
        return "".join(res)