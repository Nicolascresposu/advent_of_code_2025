# we find the max (ignoring the last one) and then we find the max one that is after it
finalNum = 0
maxRange = 13 #3 for 2, 13 for 12
def generalSplitter(charLineArray):
    global finalNum
    maxesArray = []
    global maxRange
    for i in range(1,maxRange): #we can change the range here. #so we use 3 for 2, so for 12 we would need 13
        # print(i)
        # print("Loop #" + str(i))
        if i == 1:
            maxesArray.append(maxSubFinder(charLineArray,i,-1))
            # print(maxesArray)
        else:
            maxesArray.append(maxSubFinder(charLineArray,i,maxesArray[i-2])) # as in, find the max from everywhere except the last 1 (Works for 2)
    print(maxesArray)
    resultNumber = ""
    for index in maxesArray:
        resultNumber += str(charLineArray[index])
    finalNum += int(resultNumber)

    
def maxSubFinder(charLineArray,subAmount,lastMaxIndex): #we need a way to store the index found last time... Maybe we just return that?
    global maxRange
    # print("running maxsubfinder with " + str(subAmount))
    # the lastMaxIndex+1 is because we need to start picking from the one next to the last one we found.
    #
    charLineArrayMinusLast = charLineArray[lastMaxIndex+1:len(charLineArray) - maxRange + subAmount + 1]
    maxDiscountingLastIndex = charLineArrayMinusLast.index(max(charLineArrayMinusLast))
    return maxDiscountingLastIndex + lastMaxIndex + 1 # We need to add these 2 so we get an absolute coord
    # maxDiscountingLast = charLineArrayMinusLast[maxDiscountingLastIndex]
    # We then take the max from the other half of the array



with open("C:\\Users\\nicol\\Documents\\Programming_Local\\Advent_python2025\\day3input.txt", "r") as file:
    for line in file:
        charLineArray = []
        for char in line:
            if char != "\n":
                charLineArray.append(int(char))

        generalSplitter(charLineArray)

print(finalNum)