def mergeInputs(numRange):
    for i in range(len(numRange)-1):
        if numRange[i][1] >= numRange[i + 1][1]: #my end bigger than next's end; we kill them
            numRange[i + 1][0] = 0
            numRange[i + 1][1] = numRange[i][1]
        elif numRange[i][1] >= numRange[i + 1][0]: #my end bigger than next's start; we make them start from the next one
            numRange[i + 1][0] = numRange[i][1] +1
            # numRange[i+1][1] = numRange[i][1] 
    return numRange

with open("C:\\Users\\nicol\\Documents\\Programming_Local\\Advent_python2025\\day5input.txt", "r") as file:
    numRange = []
    endList = []
    counter = 0
    for line in file:
        line = line.replace("\n","")
        # this doesn't work... I should try to just add the ranges and then compare each number after if it's bigger than another or smaller than the other one, and if there's a match we exit.
        if line.find("-") != -1:
            currNumRange = line.split("-")
            currNumRange[0] = int(currNumRange[0]) # type: ignore
            currNumRange[1] = int(currNumRange[1]) # type: ignore
            print("Adding: " + str(currNumRange[0]) + " - " + str(currNumRange[1]))
            numRange.append((currNumRange[0],currNumRange[1]))
            endList.append((currNumRange[1],currNumRange[0]))

# print(numRange) # pre-sorting
numRange.sort() #holy shit you can sort tuples
endList.sort()
for i in range(len(endList)):
    endList[i] = list(endList[i])
    temp = endList[i][0]
    endList[i][0] = endList[i][1]
    endList[i][1] = temp
for i in range(len(numRange)):
    numRange[i] = list(numRange[i])
print(numRange) # sorted
mergeInputs(numRange)
print(numRange)
# print(endList)
# for i in range(len(numRange)-1):
#     if numRange[i][1] > numRange[i+1][1]: #if our end is bigger than the other end (means we swallow them whole)
#         numRange[i+1][0] = numRange[i][0]
#         numRange[i+1][1] = numRange[i][1]

    # if numRange[i][1] < numRange[i+1][1]: #if their end is bigger than ours (means we get swalloed whole)
    #     numRange[i][0] = numRange[i+1][0]
    #     numRange[i][1] = numRange[i+1][1]
    
    # elif numRange[i][1] > numRange[i+1][0]: #if the last of ours is bigger or equal to the first of next
    #     numRange[i][1] = numRange[i+1][0] - 1
    
# print(numRange) # sorted
counter = 0
for i in range(len(numRange)):
    if numRange[i][0]!=0:
        counter += numRange[i][1] - numRange[i][0] + 1
        print(counter)