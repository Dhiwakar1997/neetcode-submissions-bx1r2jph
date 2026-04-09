class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False

        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)

        for i in range(len(s1)):
            s1_counter[s1[i]]+=1
            s2_counter[s2[i]]+=1
        
        match=0

        for i in range(ord("a"),ord('a')+26):
            if s1_counter[chr(i)]==s2_counter[chr(i)]:
                match+=1

        l=0

        for r in range(len(s1),len(s2)):
            cur = s2[r]

            if match==26: return True

            s2_counter[cur]+=1

            if s1_counter[cur]==s2_counter[cur]:
                match+=1
            elif s1_counter[cur]+1==s2_counter[cur]:
                match-=1

            cur= s2[l]
            
            s2_counter[cur]-=1

            if s1_counter[cur]==s2_counter[cur]:
                match+=1
            elif s1_counter[cur]-1==s2_counter[cur]:
                match-=1
            l+=1
        return match == 26
