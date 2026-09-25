class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        pre=1
        for i in range(n):
            answer[i]= pre
            pre*=nums[i]
            
        post=1
        for i in range(n-1,-1,-1):
            answer[i] *=post
            post *=nums[i]
        return answer