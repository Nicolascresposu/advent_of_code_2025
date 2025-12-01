lockPointer = 50
lockAt0Counter = 0
lastLockPointer = 50
with open("day1input.txt", "r") as file:
    for line in file:
        # print(line.strip())
        numberVal = int(line[1:]) #this works.
        lastLockPointer = lockPointer
        if line[0] == "L":
            lockPointer -= numberVal
        if line[0] == "R":
            lockPointer += numberVal

        print("currently at:" + line.strip())
        print("pointer at: " + str(lockPointer))

        if lockPointer > 99: #if we go over 99
            lockAt0Counter += int(lockPointer / 100)
            lockPointer = lockPointer % 100
            print("Counter at: " + str(lockAt0Counter))
        elif lockPointer < 0:
            if lastLockPointer != 0:
                lockAt0Counter += 1
            lockAt0Counter += int(-lockPointer / 100)
            lockPointer = lockPointer % 100
            print("Counter at: " + str(lockAt0Counter))
        elif lockPointer == 0:
            lockAt0Counter += 1
            print("Counter at: " + str(lockAt0Counter))
        print("------")
        # if lockPointer < 0:
        #     if lockPointer < -99:
        #         lockAt0Counter += int(-lockPointer / 100) -1
        #     else:
        #         lockAt0Counter += 1
        #     lockPointer = lockPointer % 100
        #     lockPointer += 100
        # if lockPointer >= 100:
        #     lockAt0Counter += int(lockPointer / 100) -1
        #     lockPointer = lockPointer % 100
        # if lockPointer == 0:
        #     lockAt0Counter += 1
        #     print("Lock counter increased: " + str(lockAt0Counter))
        # print("-----")
print(lockAt0Counter)