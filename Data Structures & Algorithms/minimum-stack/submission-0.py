class MinStack:

    def __init__(self):
        self.main = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.main.append(val)
        self.prefix.append(val)
        if len(self.prefix) > 1:
            self.prefix[-1] = min(val, self.prefix[-2])

    def pop(self) -> None:
        self.main.pop()
        self.prefix.pop()
        

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
        
