# python basics: list can't be key value for hash map/dict in python
# dict.get(key, 0) important for count
class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            dx, dy  = abs(px - x), abs(py - y)
            # skp non diag points
            if dx != dy or dx == 0 or dy == 0:
                continue
            # for diag points
            res += (
                self.ptsCount.get((x ,py), 0) *
                self.ptsCount.get((px ,y), 0)
            ) 
        return res
                 

            
        
