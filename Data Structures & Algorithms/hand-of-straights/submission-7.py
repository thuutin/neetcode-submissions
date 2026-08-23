class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
            
        c = Counter(hand)
        for d in sorted(hand):
            if c[d] == 0:
                continue
            count = 0
            while count < groupSize:
                c[d] -= 1
                count += 1                    
                if c[d] < 0:
                    return False
                d += 1
            
        return True