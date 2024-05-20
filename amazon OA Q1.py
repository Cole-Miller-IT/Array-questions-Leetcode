#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'makePowerNonDecreasing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#

def makePowerNonDecreasing(power):
    # Write your code here
    #This one I just don't understand what they want right now,
    #you could make the diagram a bit better to understand with having a transition arrow showing the +3 to get to the middle row
    #I think I know what they want now
    
    #Also stop with the negatives, just say asceding or descending order, not this non-descending /negation thing you got going on, 
    #it's unintuitive
    
    #aim to bring the next server to the same power as the  current server
    print(power)
    
    powerIncrease = 0
    index = 0
    for server in power:
        print(server)
        
        if power[index + 1] < power[index] and (index + 1) <= len(power) - 1:
            print("next server has less power than the current server")
            #if this is the case add power to all servers right of the current server
            AddingUnlimitedPower = True
            powerDiff = power[index] - power[index + 1]
            powerIncrease += powerDiff
            newIndex = index + 1
            while(AddingUnlimitedPower):
                #add the difference in power to all of the remaining servers
                power[newIndex] += (powerDiff)
                newIndex += 1
                
                if newIndex > len(power) - 1:
                    AddingUnlimitedPower = False
                    break
                    
    return powerIncrease
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    power_count = int(input().strip())

    power = []

    for _ in range(power_count):
        power_item = int(input().strip())
        power.append(power_item)

    result = makePowerNonDecreasing(power)

    fptr.write(str(result) + '\n')

    fptr.close()
