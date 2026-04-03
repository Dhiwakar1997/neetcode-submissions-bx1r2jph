class MinStack:

    def __init__(self):
        self.stack=[]
        self.minVal=float("inf")

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal,val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popedVal =self.stack.pop()
            if self.stack:
                self.minVal = min(self.stack)
            else:
                self.minVal = float("inf")
            return popedVal

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
