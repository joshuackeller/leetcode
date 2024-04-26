class MinStack:
    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if len(self.min_values) == 0:
            self.min_values.append(val)
        elif val <= self.min_values[-1]:
            self.min_values.append(val)

    def pop(self) -> None:
        if len(self.values) > 0:
            val = self.values[-1]
            self.values.pop()
            if len(self.min_values) > 0 and val == self.min_values[-1]:
                self.min_values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
