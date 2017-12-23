import json
data = json.load(open("data.json"))

def translate(word):
    if inputWord in data:
        return(data[word])
    else:
        return "Word doesn't exist"

inputWord = input("enter the word : ")
print(translate(inputWord))
