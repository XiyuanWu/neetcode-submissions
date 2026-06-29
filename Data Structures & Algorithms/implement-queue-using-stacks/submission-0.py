class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())

        ans = self.s.pop()

        while temp:
            self.s.append(temp.pop())

        return ans

    def peek(self) -> int:
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())

        ans = self.s[-1]

        while temp:
            self.s.append(temp.pop())

        return ans

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()