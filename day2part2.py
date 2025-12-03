import re
finalSum = 0
curr = 0
def parity(string): #This splits them into usable strings
    global finalSum
    numbers = list(map(int,string.split("-")))
    print(numbers)
    curr = numbers[0]
    max = numbers[1]
    while curr <= max: #here we start increasing numbers[0] until it matches the other one
        currstr = str(curr)
        search = re.search(r"^(\d{1})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{2})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue 
        search = re.search(r"^(\d{3})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue           
        search = re.search(r"^(\d{4})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{5})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{6})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{7})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{8})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{9})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
        search = re.search(r"^(\d{10})\1+$",currstr) #we should replace {1} with numbers until half of final num length
        if search != None:
            finalSum += int(search.group(0))
            curr+=1
            continue
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