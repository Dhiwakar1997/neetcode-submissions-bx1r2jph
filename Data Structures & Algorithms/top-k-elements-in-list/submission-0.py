class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup=defaultdict(int)

        for num in nums:
            lookup[num]+=1
        sortedNums= sorted(lookup.items(), key= lambda k:k[1],reverse=True)
        result = [k for k,val in sortedNums][:k]
        return result