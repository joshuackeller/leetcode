from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.left or num < -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)

        if len(self.left) - len(self.right) > 1:
            move = heappop(self.left)
            heappush(self.right, -move)
        elif len(self.right) - len(self.left) > 1:
            move = heappop(self.right)
            heappush(self.left, -move)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2

