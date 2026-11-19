class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = 1
        res = [1] * len(nums)
        hasZero=False
        if nums.count(0)>1:
            return [0] * len (nums)
        if 0 in nums:
            hasZero = True
        for i in range (len(nums)):
            if hasZero:
                if nums[i] != 0:
                    multi *= nums[i]
                    res[i]=0
            else:
                multi *= nums[i]
            
        for i in range (len(nums)):
            if res[i] != 0:
                if nums[i] !=0:
                    res[i]=int(multi/nums[i])
                else:
                    res[i]=int(multi)

        return res


            
            


