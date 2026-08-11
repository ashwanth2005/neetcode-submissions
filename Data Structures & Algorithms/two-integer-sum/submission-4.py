class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Line 1: Initialize an empty hash map
        
        for i, num in enumerate(nums):  # Line 2: Loop through the array with indices
            diff = target - num         # Line 3: Calculate the required complement
            
            if diff in seen:            # Line 4: Check if the complement is already in our map
                return [seen[diff], i]  # Line 5: If found, return the saved index and current index
            
            seen[num] = i               # Line 6: Otherwise, store current number and its index