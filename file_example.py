

import re
newdata=""

def mult85(match):
    num=int(match.group())
    return str(num*85)
with open ("data.text", "r+",encoding='utf-8') as fh:
    for line in fh:
        
        match=re.sub("\d+",mult85,line)
        print(match)
        match=re.sub("\$",chr(8377),match)
        newdata=newdata+match

        
        

with open("data.text","r+",encoding='utf-8') as fh:
    fh.write(newdata)
