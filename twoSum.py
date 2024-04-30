from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Convert list to a dictionary to speed up lookups
        #remove all values that can't be part of the solution, numbers greater than or equal to the target
        myDict = {}
        index = 0
        for num in nums:
            if num < target:
                #add to dict
                myDict.update({num: index})

            index += 1

        #print("===========================")
        #print("target: " + str(target))
        #print("My dict: " + str(myDict))


        #for every value in the new dictrionary
        #print(myDict.keys())
        for key in myDict:
            #print("Key: " + str(key))
            #target - value = possible second value
            possibleSecondNum = target - key
            #print("Possible second is: " + str(possibleSecondNum))
            
            #does this value exist in the dictionary
            possibleSecond = myDict.get(possibleSecondNum)
            #print(possibleSecond) #index
            if possibleSecond != None:
                #print("found")
                #yes, found the two indexes that make the target
                #print("possible second" + str(possibleSecond))
                if myDict[key] == possibleSecond:
                    #the two numbers added together are the same number
                    #Find the first index in the nums list
                    index = 0
                    for num in nums:
                        if num == key:
                            firstIndex = index
                            break

                        index += 1

                    secondIndex = possibleSecond

                else:
                    firstIndex = myDict[key]
                    secondIndex = possibleSecond

                return [firstIndex, secondIndex]
            #else:
                #print("value doesn't exist, checking next")
                #no, keep searching


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

nums = [0,2,1,7,8,10,45,43,3,89,3,0,43,76]
target = 6
print(Solution.twoSum(Solution, nums, target))