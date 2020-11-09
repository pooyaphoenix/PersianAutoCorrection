import nltk
import re

def read_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        file_name_data = f.read()
        file_name_data=file_name_data.lower()
        words = re.findall('\w+',file_name_data)
    return words


words=read_file('text.txt')
probs={}

x= input("type something: ").split()[0]
if x not in words:
    for word in words:
        probs[word]= (nltk.edit_distance(x,word))
        #print(word,probs[word])

    print(f"did you mean {min(probs, key=probs.get)}?")

else:
    print(x)


