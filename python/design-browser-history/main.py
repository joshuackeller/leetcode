class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_visit = ListNode(url, self.cur)
        self.cur.next = new_visit
        self.cur = new_visit
        
    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next
        
        return self.cur.val

        
         
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

bh = BrowserHistory("leetcode.com")
print()
print(bh.visit("google.com"))
print()
print(bh.visit("facebook.com"))
print()
print(bh.visit("youtube.com"))
print()
print(bh.back(1))
print()
print(bh.back(1))
print()
print(bh.forward(1))
print(bh.visit("linkedin.com"))
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))