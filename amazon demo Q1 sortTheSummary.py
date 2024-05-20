#!/bin/python3

import math
import os
import random
import re
import sys

#works but is very inefficient

#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def groupSort(arr):
    # Write your code here
    #print(arr)
    myArr = []
    
    #go through each element of the array
    myDict = {}
    for element in arr:
        #print(element)
        #add the value to a dict and increase the cound by 1
        myDict[element] = myDict.get(element, 0) + 1
        
    print(myDict)
    
    #for every value in the dictionary
    for pair in myDict:
        #print("Unique val: " + str(pair) + " freq. " + str(myDict[pair]))
        #make a 2D array that holds the value and the count 
        #add every value to the final array at random
        myArr.append([pair, myDict[pair]])
        
    print(myArr)
    
    #sort based on the frequency until no swaps occur (descending)
    sorting = True
    while(sorting):
        #print("while -----------")
        index = 0
        previousPair = None
        swapOccurred = False
        for pair in myArr:
            #print("for #######")
            if previousPair != None:
                #print(pair)
                #print(previousPair)
                
                #If the current frequency is greater than the previous frequency, swap
                if pair[1] > previousPair[1]:
                    #swap the two values
                    swapOccurred = True
                    myArr[index - 1], myArr[index] = myArr[index], myArr[index - 1]
                    #myArr[index - 1] = pair
                    #myArr[index] = previousPair
            
            index += 1
            previousPair = pair
            
        if swapOccurred == False:
            break
    
    print(myArr)
    
    #sort based on unique values in each frequency group until no swaps occur(ascending)
    sorting = True
    while(sorting):
        #print("while ==============")
        index = 0
        previousPair = None
        swapOccurred = False
        for pair in myArr:
            #print("for @@@@@@")
            if previousPair != None:
                #print(pair)
                #print(previousPair)
                
                #if the frequncies are the same
                if pair[1] == previousPair[1]:
                    #If the current frequency is greater than the previous frequency, swap
                    if pair[0] < previousPair[0]:
                        #swap the two values
                        swapOccurred = True
                        myArr[index - 1], myArr[index] = myArr[index], myArr[index - 1]
                        #myArr[index - 1] = pair
                        #myArr[index] = previousPair
            
            index += 1
            previousPair = pair
            
        if swapOccurred == False:
            break
    
    print(myArr)
    
    return myArr
    
    
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = groupSort(arr)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
