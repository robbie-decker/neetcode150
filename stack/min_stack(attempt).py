# MY SOLUTION WAS FASTER AND BETTER MEMORY
class MinStack:

    def __init__(self):
        self.stack = []
        self.myMin = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.myMin:
            self.myMin.append(val)
        else:
            if self.myMin[-1] >= val:
                self.myMin.append(val)
    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.myMin[-1]:
            self.myMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.myMin[-1]