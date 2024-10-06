numWords = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

userInput = input("Enter some figure: ")
outPut = ""

for num in userInput:
    if num == "0":
        outPut += numWords[0] + " "
    if num == "1":
        outPut += numWords[1] + " "
    if num == "2":
        outPut += numWords[2] + " "
    if num == "3":
        outPut += numWords[3] + " "
    if num == "4":
        outPut += numWords[4] + " "
    if num == "5":
        outPut += numWords[5] + " "
    if num == "6":
        outPut += numWords[6] + " "
    if num == "7":
        outPut += numWords[7] + " "
    if num == "8":
        outPut += numWords[8] + " "
    if num == "9":
        outPut += numWords[9] + " "
print(outPut)