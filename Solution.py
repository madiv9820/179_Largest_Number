from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator function for sorting
        def compare(s1, s2):
            # Concatenate in two possible orders
            if s1 + s2 > s2 + s1:
                return -1  # Return -1 if s1 should come before s2
            elif s1 + s2 < s2 + s1:
                return 1   # Return 1 if s2 should come before s1
            else:
                return 0   # Return 0 if s1 and s2 are equal in both concatenation orders
        
        # Convert all numbers to strings for easier concatenation and comparison
        nums = [str(x) for x in nums]
        
        # Sort the numbers using the custom comparator
        nums.sort(key = cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        result = ''.join(nums)
        
        # Edge case: If the largest number is '0', return '0'
        if result[0] == '0':
            return '0'
        
        return result