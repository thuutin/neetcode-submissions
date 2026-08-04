class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        minValue = val
        if len(self.st) > 0:
            minValue = min(minValue, self.st[-1][1])
        self.st.append( (val, minValue) )

    def pop(self) -> None:
        self.st.pop()[0]
        

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
