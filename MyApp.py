import json
from difflib import  get_close_matches
data = json.load(open("data.json"))

def findWord(word):
    word = word.lower()     #making word case insensitive
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("\nDid you mean %s instead ? if yes 'Y' or no 'N' : " % get_close_matches(word,data.keys())[0])
        if (yn == 'Y') or (yn == 'y'):
            return data[get_close_matches(word,data.keys())[0]]
        elif (yn == 'N') or ( yn == 'n'):
            return "Word Doesn't exists"
        else:
            return "Wrong input"
    else:
        return "Word doesn't exist"

inputWord = input("enter the word : ")
output = findWord(inputWord)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
