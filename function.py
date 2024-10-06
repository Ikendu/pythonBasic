def numWord(userInput):
    emoji = {
    '(:': '😊',
    ':)': '😊',
    ':(': '😌',
    '):': '😌',
    }   
    userInput = userInput.split(" ")

    output = ""
    for ch in userInput:
        output += emoji.get(ch, ch) + " "
        
    return output



message = input("Enter a message: ")

outcome =  numWord(message)
print(outcome)