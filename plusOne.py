from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        adding = True
        while(adding):
            #print("current digit at index " + str(index))
            #print(digits[index])

            if digits[index] == 9:
                #print("== 9")
                digits[index] = 0
                index -= 1
                if index < 0:
                    #print("insert")
                    digits.insert(0, 1)
                    adding = False
                    return digits


            else:
                digits[index] += 1
                index -= 1
                adding = False
                return digits



digits = [5,9]
print(Solution.plusOne(Solution, digits))