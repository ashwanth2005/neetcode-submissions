class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count=0
        n=set(nums)
        for num in n:
            if(num-1) not in n:
                count=1
                while num+count in n:
                    count+=1
                max_count=max(count,max_count)
        return max_count
