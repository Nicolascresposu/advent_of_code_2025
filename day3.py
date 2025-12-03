finalNum = 0
with open("day3input.txt", "r") as file:
    for line in file:
        charLineArray = []
        for char in line:
            if char != "\n":
                charLineArray.append(int(char))
        # print(charLineArray)
        charLineArrayMinusLast = charLineArray[:len(charLineArray)-1]
        maxDiscountingLastIndex = charLineArrayMinusLast.index(max(charLineArrayMinusLast))
        maxDiscountingLast = charLineArrayMinusLast[maxDiscountingLastIndex]
        # We then take the max from the other half of the array
        charLineFromMaxFound = charLineArray[maxDiscountingLastIndex+1:]
        charLineFromMaxFoundMax = charLineFromMaxFound[charLineFromMaxFound.index(max(charLineFromMaxFound))]

        # print(charLineFromMaxFound)
        # print(maxDiscountingLast)
        # print(charLineFromMaxFoundMax)
        finalNum += int(str(maxDiscountingLast) + str(charLineFromMaxFoundMax))
        print(int(str(maxDiscountingLast) + str(charLineFromMaxFoundMax)))
print(finalNum)