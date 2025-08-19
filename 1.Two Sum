class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number:index pairs
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            # Check if complement exists in the dictionary
            if complement in seen:
                return [seen[complement], i]
            # Add current number and its index to the dictionary
            seen[num] = i
        
        # No solution found (though problem guarantees one)
        return []
