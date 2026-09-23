import bisect
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        c = 1
        while stack and price >= stack[-1][0]:
            x, cc = stack.pop()
            c += cc
        stack.append( (price, c) )
        return c





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)