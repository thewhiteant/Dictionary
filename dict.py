import json
from difflib import get_close_matches


file  =  open('dictionary.json')
data = json.load(file)

def retrans(word):
    fword = word.lower()
    if fword in data:
        return data[fword]
    elif len(get_close_matches(fword,data.keys())) > 0 :
        yn = input(f"Is This Closer To {get_close_matches(fword,data.keys())[0]} ? (Y or N ) :  ")
        if yn.lower() == "y":
            return data[get_close_matches(fword, data.keys())[0]]
        else :
            return "Sorry Not Found"
    else:
        return "Word Not Found"


print("<============Whiteant Ting ting Dictionary===========>")
matchword = input("Word: ")
result = retrans(matchword)
print(result)

