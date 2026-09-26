from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set (1) in xor_all
        # This bit is different between the two unique numbers
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition the array into two groups and find the unique number in each group
        num1 = 0
        num2 = 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
