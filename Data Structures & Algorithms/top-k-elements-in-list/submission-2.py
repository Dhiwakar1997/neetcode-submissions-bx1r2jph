class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        data = dict(sorted(counter.items(),key= lambda item:item[1],reverse=True))
        ans=list(data.keys())[:k]
        return ans