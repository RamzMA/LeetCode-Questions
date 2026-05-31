from collections import deque


class MyStack:
    """
    Implement Stack using Queues - #225

    Use a deque with only queue operations (append and popleft).
    On each push, rotate the queue len-1 times so the newest element ends up at the front.
    This makes popleft behave like a stack pop.

    Time complexity: O(n) for push, O(1) for pop, top, empty
    Space complexity: O(n)
    """

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# test cases
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # 3
print(stack.pop())  # 3
print(stack.top())  # 2
print(stack.empty())  # False
stack.pop()
stack.pop()
print(stack.empty())  # True
