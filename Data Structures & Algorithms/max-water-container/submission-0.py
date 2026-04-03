class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        res=0

        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            res=max(res,area)

            if heights[l]<heights[r]:
                l+=1
            elif  heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
        return res