class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resu=[]
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if j!=i:
                    res=res*nums[j]
            resu.append(res)
        return resu