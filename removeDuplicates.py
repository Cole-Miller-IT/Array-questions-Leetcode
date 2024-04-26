from typing import List

class Solution:
    #Given an integer array nums sorted in ascending order, remove the duplicates in-place such that each unique element appears only once. 
    #The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0
        end = False
        for num in nums:
            #print("-------------------------------")
            nextI = i + 1

            #print(i)
            #print(nextI)
            #print(len(nums))
            if nextI >= len(nums):
                #print("last value")
                break

            searching = True
            while(searching):
                if nextI >= len(nums):
                    #print("final value found")
                    replacementValue = 69

                    numDuplicates = (nextI - 1) - i
                    duplicateIndex = i + 1
                    for duplicate in range(numDuplicates):
                        nums[duplicateIndex] = replacementValue
                        duplicateIndex = duplicateIndex + 1

                    searching = False
                    end = True
                    k = k + 1
                    #print(nums)
                    break



                #print("current number: " + str(nums[i]))
                #print("next number: " + str(nums[nextI]))

                if nums[nextI] == nums[i]:
                    #print("duplicate found")
                    nextI = nextI + 1 #move forward

                else:
                    #print("next different found: " + str(nums[nextI]))
                    replacementValue = nums[nextI]

                    #Replace the duplicates with the next different value
                    #print("Num of duplicates found: " + str((nextI - 1) - i))
                    #print("from indices: " + str(i + 1) + " to " + str((nextI - 1)))

                    numDuplicates = (nextI - 1) - i
                    duplicateIndex = i + 1
                    for duplicate in range(numDuplicates):
                        nums[duplicateIndex] = replacementValue
                        duplicateIndex = duplicateIndex + 1

                    searching = False
                    k = k + 1
                    #print(nums)


            if end == True:
                return k

            i = i + 1

            





#nums = [0,0,1,1,1,2,2,3,3,4,5,6,6]
nums = [-100, -100, -50, 0, 50, 100, 100]
k = Solution.removeDuplicates(Solution, nums)
print(k)