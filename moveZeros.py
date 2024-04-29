from typing import List

class Solution:
    #Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    #Note that you must do this in-place without making a copy of the array.
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            print("lenght 1")
 
        else: #two or more items in the list
            #print("========================")
            currentIndex = 0
            nextIndex = currentIndex + 1
            lastIndex = len(nums) - 1

            rearranging = True
            while(rearranging):
                #print("---------------------------------")
                #print(nums)
                #print("current index: " + str(currentIndex))
                #print("next index: " + str(nextIndex))

                if nums[currentIndex] == 0:
                    #Check the next value
                    if nums[nextIndex] != 0:
                        #swap the values, moving the zero down the array to the right
                        #print("Swap")
                        nums[currentIndex] = nums[nextIndex]
                        nums[nextIndex] = 0

                        #move down the array to the next value to check
                        currentIndex += 1
                        nextIndex = currentIndex + 1  

                    else:
                        #next value found was a 0, keep looking
                        #print("keep looking")
                        nextIndex += 1

                    #if we reached the last value, swap it with the current value. 0 will have no effect, but if the last value is not 0 then it will matter
                    if nextIndex >= lastIndex:
                            #print("end1")
                            tempVal = nums[currentIndex]
                            nums[currentIndex] = nums[lastIndex]
                            nums[lastIndex] = tempVal
                            rearranging = False
                            break  

                else:
                    #step over non-zero numbers
                    #print("step over")
                    currentIndex += 1
                    nextIndex = currentIndex + 1  

                    if nextIndex > lastIndex:
                        #print("end2")
                        rearranging = False
                        break 


nums = [6,0,1,0,3,12,0,4,0]
Solution.moveZeroes(Solution, nums)
print(nums)

nums1 = [6]
Solution.moveZeroes(Solution, nums1)
print(nums1)

nums2 = [0]
Solution.moveZeroes(Solution, nums2)
print(nums2)

nums3 = [0, 1]
Solution.moveZeroes(Solution, nums3)
print(nums3)

nums4 = [1, 0]
Solution.moveZeroes(Solution, nums4)
print(nums4)

nums5 = [0,1,0,3,12]
Solution.moveZeroes(Solution, nums5)
print(nums5)