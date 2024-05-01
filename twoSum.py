from typing import List

class Solution:
    #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    #You may assume that each input would have exactly one solution, and you may not use the same element twice.
    #You can return the answer in any order.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Convert list to a dictionary to speed up lookups
        #remove all values that can't be part of the solution, numbers greater than or equal to the target
        myDict = {}
        duplicates = set()
        index = 0
        for num in nums:
            if myDict.get(num) != None:
                duplicates.add(num)

            #add to dict
            myDict.update({num: index})

            index += 1

        print("===========================")
        print("target: " + str(target))
        print("My dict: " + str(myDict))
        print("dupes: " + str(duplicates))


        #for every value in the new dictrionary
        for key in myDict:
            #target - value = possible second value
            possibleSecondNum = target - key
            
            if possibleSecondNum == key:
                #looking for a duplicate value
                if possibleSecondNum in duplicates:
                    index = 0
                    for num in nums:
                        if num == possibleSecondNum:
                            #print("dupes return")
                            firstIndex = index
                            secondIndex = myDict[key]
                            return [firstIndex, secondIndex]
                        
                        index += 1
                else:
                    #this is not part of the solution
                    continue

            #does this value exist in the dictionary
            possibleSecond = myDict.get(possibleSecondNum)
            if possibleSecond != None:
                #print("value exists")   
                firstIndex = myDict[key]
                secondIndex = possibleSecond
                return [firstIndex, secondIndex]
            
            #else:
                #keep searching


'''
nums = [2,4,5,11,15]
target = 9
print(Solution.twoSum(Solution, nums, target))

nums = [2,7,11,15]
target = 9
print(Solution.twoSum(Solution, nums, target))

nums = [3,2,4]
target = 6
print(Solution.twoSum(Solution, nums, target))

nums = [3,3]
target = 6
print(Solution.twoSum(Solution, nums, target))

nums = [3,4,1,8,3]
target = 6
print(Solution.twoSum(Solution, nums, target))'''

nums = [0,4,3,0]
target = 0
print(Solution.twoSum(Solution, nums, target))

nums = [-3,4,3,90]
target = 0
print(Solution.twoSum(Solution, nums, target))