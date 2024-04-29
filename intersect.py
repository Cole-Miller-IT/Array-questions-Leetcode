from typing import List

class Solution:
    #Given two integer arrays nums1 and nums2, return an array of their intersection. 
    #Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seenDict = {}
        returnList = []

        for num in nums1:
            if num in seenDict:
                seenDict.update({num: seenDict[num] + 1})
            else:
                seenDict.update({num: 1})
        

        print(seenDict)

        for num2 in nums2:
            if num2 in seenDict:
                print(num2)
                returnList.append(num2)

                seenDict.update({num2: seenDict[num2] - 1})

                if seenDict[num2] == 0:
                    print("pop")
                    seenDict.pop(num2)


        print(seenDict)

        return returnList


nums1 = [1,2,2,1,3]
nums2 = [2,2,1,5]
print(Solution.intersect(Solution, nums1, nums2))