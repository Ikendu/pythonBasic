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

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)