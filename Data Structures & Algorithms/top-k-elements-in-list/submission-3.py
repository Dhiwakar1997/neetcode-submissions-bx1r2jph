class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ans = [i for i,v in counter.most_common(k) ]
        return ans