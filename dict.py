import json


file  =  open('dictionary.json')
data = json.load(file)

def retrans(word):
    return data[word]
    


print("<============Whiteant Ting ting Dictionary===========>")
matchword = input("Word: ")
result = retrans(matchword)
print(result)
