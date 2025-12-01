lockPointer = 50
lockAt0Counter = 0
with open("day1input.txt", "r") as file:
    for line in file:
        # print(line.strip())
        numberVal = int(line[1:]) #this works.
        if line[0] == "L":
            lockPointer -= numberVal
        if line[0] == "R":
            lockPointer += numberVal
        if lockPointer < 0:
            lockPointer = lockPointer % 100
            lockPointer += 100
        if lockPointer >= 100:
            lockPointer = lockPointer % 100
        if lockPointer == 0:
            lockAt0Counter += 1
            print("Lock counter increased: " + str(lockAt0Counter))
        print("currently at:" + line.strip())
        print("pointer at: " + str(lockPointer))
print(lockAt0Counter)