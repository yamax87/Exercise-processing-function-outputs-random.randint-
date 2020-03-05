#make sure getRandom() is only called when we want the random number to change (ie, at the beginning of the game).
#Otherwise, we just want the value of x, and we want it to stay the same. 

import random


def getRandom():

    randomNum = random.randint(0,100)

    print(randomNum)
    return randomNum


def processRandom1(inputInt):

    print('processRandom1 returned the value: ' , inputInt)

def processRandom2(inputInt):

    print('processRandom2 returned the value: ' , inputInt)

def processRandom3(inputInt):

    print('processRandom3 returned the value: ' , inputInt)



x = getRandom()

processRandom1(x)
processRandom2(x)
processRandom3(x)  #should all be the same. 
