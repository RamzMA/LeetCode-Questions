class MinStack:
    """
    Min Stack - #155

    Use two stacks one for values, one for minimums.
    On each push, record the current minimum in the min stack.
    On pop, both stacks pop together restoring the previous minimum automatically.

    Time complexity: O(1)
    Space complexity: O(n)
    """

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minval = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# test cases
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())  # -3
stack.pop()
print(stack.top())  # 0
print(stack.getMin())  # -2
stack.push(1)
print(stack.getMin())  # -2
print(stack.top())  # 1
