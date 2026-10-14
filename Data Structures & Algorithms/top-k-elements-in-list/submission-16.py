class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pairs = list(count.items())
        pairs.sort(key=lambda x: -x[1])
        top_k = pairs[:k]
        res = []
        for key,value in top_k:
            res.append(key)
        return res