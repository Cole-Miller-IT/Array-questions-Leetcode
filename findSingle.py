from typing import List

class Solution:
    #Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    #You must implement a solution with a linear runtime complexity and use only constant extra space.
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return seen.pop()



nums = [4,1,2,1,2]
print(Solution.singleNumber(Solution, nums))