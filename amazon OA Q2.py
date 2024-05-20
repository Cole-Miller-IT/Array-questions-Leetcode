#!/bin/python3

import math
import os
import random
import re
import sys


#Amazon OA Q2 2024
#
# Complete the 'numIdleDrives' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY y
#

def numIdleDrives(x, y):
    # Write your code here
    
    if len(x) == 0:
        return 0
        
    if len(y) == 0:
        return 0
        
    if len(x) != len(y):
        return 0
        
    print(x)
    print(y)
    
    
    numIdleRobots = 0
    above = False
    below = False
    left = False
    right = False
    
    #go through all of the drives
    curIndex = 0
    for curDrive in x:
        #print("----------------------------")
        #print("Current Drive: (" + str(x[curIndex]) + "," + str(y[curIndex]) + ")")
        
        # go through all of the drives and check if the following 4 conditions are all met by the end
        otherIndex = 0
        for otherX in x:
            #print("Other Index: " + str(x[otherIndex]) + "," + str(y[otherIndex]))
            #Skip itself
            #if otherIndex == curIndex:
                #continue
            
            #To be idle 4 conditions must be satisfied
            #A drive is below the current Drive
                #below current drive if a drive has x == currentDrive and y < current drive
            if x[otherIndex] == x[curIndex] and y[otherIndex] < y[curIndex]:
                #print("below because of  " + str(x[otherIndex]) + "," + str(y[otherIndex]))
                below = True
            
            #A drive is above the current drive
                #above current drive if a drive has x == currentDrive and y > current drive
            if x[otherIndex] == x[curIndex] and y[otherIndex] > y[curIndex]:
                #print("above because of  " + str(x[otherIndex]) + "," + str(y[otherIndex]))
                above = True
            
            #A drive is left of the current drive
                #left current drive if a drive has x < currentDrive and y == current drive
            if x[otherIndex] < x[curIndex] and y[otherIndex] == y[curIndex]:
                #print("left because of  " + str(x[otherIndex]) + "," + str(y[otherIndex]))
                left = True
            
            #A drive is right of the current drive
                #right current drive if a drive has x > currentDrive and y == current drive
            if x[otherIndex] > x[curIndex] and y[otherIndex] == y[curIndex]:
                #print("right because of  " + str(x[otherIndex]) + "," + str(y[otherIndex]))
                right = True
                
            otherIndex += 1
            
        #if 4 conditions are met, add to the array of idle drives 
        if above == True:
            if below == True:
                if left == True: 
                    if right == True:
                        #drive is idle
                        #print("idleRobot at (" + str(x[curIndex]) + "," + str(y[curIndex]) + ")")
                        numIdleRobots += 1
                        
        
        #Reset
        above = False
        below = False
        left = False
        right = False
        curIndex += 1
    
    return numIdleRobots
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    result = numIdleDrives(x, y)

    fptr.write(str(result) + '\n')

    fptr.close()
