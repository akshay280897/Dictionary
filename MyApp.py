import json
from difflib import  get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()     #making word case insensitive
    if word in data:
        return(data[word])
    elif len(get_close_matches(word,data.keys())) > 0:
        return "\nDid you mean %s " % get_close_matches(word,data.keys())[0]
    else:
        return "Word doesn't exist"

inputWord = input("enter the word : ")
print(translate(inputWord))
