from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        numsLength = len(nums)

        if k != 0:
            for step in range(k):
                index = 0
                value = int(nums[index])
                for number in nums:
                    #Determine new index position
                    #newIndex = (index + k) % numsLength
                    newIndex = (index + 1) % numsLength

                    #shift value
                    tempVal = int(nums[newIndex])
                    nums[newIndex] = value
                    value = tempVal
                
                    index += 1



nums = [-1,-100,3,99,6]
k = 5
Solution.rotate(Solution, nums, k)
print(nums)


nums = [-1,-100,3,99,6,7]
k = 1
Solution.rotate(Solution, nums, k)
print(nums)