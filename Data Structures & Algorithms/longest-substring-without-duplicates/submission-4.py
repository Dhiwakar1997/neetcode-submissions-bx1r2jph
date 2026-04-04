class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        charMap={}
        l=0
        res=0

        for r, char in enumerate(s):
            if char in charMap and charMap[char]>=l:
                l = charMap[char]+1
            charMap[char]=r
            res=max(res,r-l+1)

        return res

