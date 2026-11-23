class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for n in nums:
            counts[n]=counts.get(n,0) + 1

        heap = [(count,num) for num,count in counts.items()]
        heapq.heapify_max(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res
