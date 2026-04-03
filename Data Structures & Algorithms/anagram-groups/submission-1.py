from collections import defaultdict
import hashlib
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_hash(text:str)->bool:
            count=[0]*26
            for t in text:
                count[ord(t)-ord('a')]+=1
            return tuple(count)
        
        lookup=defaultdict(list)
        for val in strs:
            hash = get_hash(val)
            lookup[hash].append(val)

        return list(lookup.values())