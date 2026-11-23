class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        resR=[1]*n
        prefix=1
        for i in range(len(nums)):
            resR[i]*=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            resR[i]*=suffix
            suffix*=nums[i]
        return resR
            





            
            


