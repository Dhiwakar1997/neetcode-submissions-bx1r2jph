class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        c = collections.Counter(s)

        for _t in t:

            if _t in c:
                c[_t]-=1
            else:
                return False

            if c[_t]<0:
                return False
        for k in c.values():
            if k>0:
                return False
        
        return True

