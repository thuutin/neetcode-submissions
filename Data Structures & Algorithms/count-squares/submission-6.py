class CountSquares:

    def __init__(self):
        self.plus = defaultdict(list)
        self.minus = defaultdict(list)
        self.points = defaultdict(int)


    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        if self.points[(x, y)] == 1:
            self.plus[y + x].append(point)
            self.minus[y - x].append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for x1, y1 in self.plus[y + x]:
            if x1 == x:
                continue
            count += self.points[(x1, y1)] * self.points[(x1, y)] * self.points[(x, y1)]
        for x1, y1 in self.minus[y - x]:
            if x1 == x:
                continue
            count += self.points[(x1, y1)] * self.points[(x1, y)] * self.points[(x, y1)]
        return count

