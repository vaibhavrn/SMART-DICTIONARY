import json
from difflib import get_close_matches

data=json.load(open("dictionary.json"))
def call(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        opt=int(input("did you mean %s(0/1)"%get_close_matches(w,data.keys())[0]))
        if opt==1:
           return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Fuck OFF!!!!!"

    else:
        return "word matched 0%! NO such word "
word=input("enter the word:")
print(call(word))
