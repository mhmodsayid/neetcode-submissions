class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        res=[]
        bucketCount = [[] for _ in range(len(nums)+1)]
        for num,val in counts.items():
            bucketCount[val].append(num)

        for c in range(len(bucketCount)-1,-1,-1):
            if len(res) == k:
                return res
            counLen = len(bucketCount[c])
            if counLen != 0:
                res.extend(bucketCount[c])






