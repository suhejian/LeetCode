class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            # 新的最小元素
            self.minstack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def min(self) -> int:
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()