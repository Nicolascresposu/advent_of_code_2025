# duplicateIdToRemove = []
changesHappened = False
def mergeAndRemoveDupes(numRange):
    global changesHappened
    while changesHappened:
        changesHappened = False
        for i in range(len(numRange)):
            updateLinks(numRange,numRange[i],False)
    # This part removes dupes
    # We turn it into tuples, then into sets, then back to lists.
        for i in range(len(numRange)):
            numRange[i] = tuple(numRange[i])
        numRange = set(numRange)
        numRange = list(numRange)
        for i in range(len(numRange)):
            numRange[i] = list(numRange[i])
def updateLinks(numRange,currNumRange,recursiveCall):
    global changesHappened
    for i in range(len(numRange)):
        pair = numRange[i]
        if currNumRange[0] == pair[0]: #if they both start at x?
            if pair[1] < currNumRange[1]: #the non editable end is bigger
                numRange[i][1] = currNumRange[1]
        if currNumRange[1] == pair[1]: #if they both end at x?
            if pair[0] < currNumRange[0]: #the non editable start is bigger
                numRange[i][0] = currNumRange[0]
        if currNumRange == pair:
            return
        elif currNumRange[0] >= pair[0] and currNumRange[0] <= pair[1] and currNumRange[1] >= pair[1]: #left is within the range of another, and right is bigger than range.
            print("Merging " + str(currNumRange) + " into " + str(numRange[i]))
            if numRange[i][1] != currNumRange[1]:
                changesHappened = True
            numRange[i][1] = currNumRange[1] #so we update the right one to the biggest one, and we run the function again.
            updateLinks(numRange,numRange[i],True)
            # updateLinks(numRange,currNumRange,True)
            return
        elif currNumRange[1] >= pair[0] and currNumRange[1] <= pair[1] and currNumRange[0] <= pair[0]: #right is within range of another, and left is smaller than range
            print("Merging " + str(currNumRange) + " into " + str(numRange[i]))
            if numRange[i][0] != currNumRange[0]:
                changesHappened = True
            numRange[i][0] = currNumRange[0] #so we update the left one to the smallest one, and we run the function again.
            updateLinks(numRange,numRange[i],True)
            # updateLinks(numRange,currNumRange,True)
            return
    if not recursiveCall:
        numRange.append([currNumRange[0],currNumRange[1]])
            



with open("C:\\Users\\nicol\\Documents\\Programming_Local\\Advent_python2025\\day5input.txt", "r") as file:
    numRange = []
    counter = 0
    for line in file:
        line = line.replace("\n","")
        # this doesn't work... I should try to just add the ranges and then compare each number after if it's bigger than another or smaller than the other one, and if there's a match we exit.
        if line.find("-") != -1:
            currNumRange = line.split("-")
            currNumRange[0] = int(currNumRange[0]) # type: ignore
            currNumRange[1] = int(currNumRange[1]) # type: ignore
            print("Adding: " + str(currNumRange[0]) + " - " + str(currNumRange[1]))
            updateLinks(numRange,currNumRange,False)

            
            # while currNumRange[0] <= currNumRange[1]:
            #     numRange.add(currNumRange[0])
            #     currNumRange[0] += 1
            
        elif line != "":
            continue
    print(numRange)
    print(counter)
    # print(duplicateIdToRemove)
    for i in range(len(numRange)):
        numRange[i] = tuple(numRange[i])
    numRange = set(numRange)
    print(numRange)
    numRange = list(numRange)
    for i in range(len(numRange)):
        numRange[i] = list(numRange[i])
    for i in range(len(numRange)): #maybe we just rerun it?
        updateLinks(numRange,numRange[i],False)
    # we now gotta count the stuff in our ranges
    mergeAndRemoveDupes(numRange)
    for i in range(len(numRange)):
        counter += numRange[i][1] - numRange[i][0] + 1
        print(counter)
