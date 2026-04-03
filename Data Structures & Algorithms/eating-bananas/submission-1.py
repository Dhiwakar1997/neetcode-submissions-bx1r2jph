class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        minVal=max(piles)

        while l<=r:
            k = (l+r)//2
            hourTaken=0
            for p in piles:
                hourTaken+= math.ceil(p/k)

            if hourTaken<=h:
                minVal=min(minVal,k)
                r=k-1
            else:
                l=k+1
        return minVal