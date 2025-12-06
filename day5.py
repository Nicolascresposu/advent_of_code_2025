with open("C:\\Users\\nicol\\Documents\\Programming_Local\\Advent_python2025\\day5input.txt", "r") as file:
    numRange = []
    counter = 0
    for line in file:
        line = line.replace("\n","")
        # this doesn't work... I should try to just add the ranges and then compare each number after if it's bigger than another or smaller than the other one, and if there's a match we exit.
        if line.find("-") != -1:
            currNumRange = line.split("-")
            currNumRange[0] = int(currNumRange[0])
            currNumRange[1] = int(currNumRange[1])
            print("Adding: " + str(currNumRange[0]) + " - " + str(currNumRange[1]))
            numRange.append([currNumRange[0],currNumRange[1]])
            # while currNumRange[0] <= currNumRange[1]:
            #     numRange.add(currNumRange[0])
            #     currNumRange[0] += 1
            
        elif line != "":
            currNum = int(line)
            for pair in numRange:
                # print("Comparing: " + str(currNum))
                if currNum >= pair[0] and currNum <= pair[1]:
                    print("Match! " + str(currNum) + " in " + str(pair))
                    counter += 1
                    break
    print(numRange)
    print(counter)