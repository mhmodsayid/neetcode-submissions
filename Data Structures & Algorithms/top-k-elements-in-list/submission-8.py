class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        res=[]
        bucketCount = [[] for _ in range(len(nums)+1)]
        for num,val in counts.items():
            bucketCount[val].append(num)

        for c in range(len(bucketCount)-1,0,-1):
            for b in bucketCount[c]:
                res.append(b)
                if len(res) == k:
                    return res
        return res






