class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res=0

        l=0
        maxf=1
        counter = defaultdict(int)

        for r in range(n):

            counter[s[r]]+=1
            maxf=max(maxf,counter[s[r]])

            while (r-l+1) - maxf > k:
                counter[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res