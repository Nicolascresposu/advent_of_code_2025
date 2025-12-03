finalSum = 0
def parity(string): #This splits them into usable strings
    global finalSum
    numbers = list(map(int,string.split("-")))
    print(numbers)
    curr = numbers[0]
    max = numbers[1]
    while curr <= max: #here we start increasing numbers[0] until it matches the other one
        # IT WAS AN EQUAL SIGN WHAT I MISSED. FUCK
        currstr = str(curr)
        # if len(str(curr)) % 2 != 0: #if it's not even-sized, we need not bother.
        #     curr+=1
        #     continue
        # currstr[:len(currstr)/2] #the splitting point
        if (currstr[:int(len(currstr)/2)] == currstr[int(len(currstr)/2):]):
            finalSum += curr
            print(curr)
        # print(curr)
        # print(currstr[:int(len(currstr)/2)])
        # print(currstr[int(len(currstr)/2):])
        curr+=1
        # print(curr)
with open("day2input.txt", "r") as file:
    numbers = file.read().split(",")
    # print(string)
    for string in numbers:
        parity(string)
print(finalSum)