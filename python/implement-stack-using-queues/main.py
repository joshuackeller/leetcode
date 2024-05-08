from collections import deque


class MyStack:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        for _ in range(len(self.s) - 1):
            self.s.append(self.s.popleft())

        return self.s.popleft()

    def top(self) -> int:
        for _ in range(len(self.s) - 1):
            self.s.append(self.s.popleft())

        answer = self.s.popleft()
        self.s.append(answer)
        return answer

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
