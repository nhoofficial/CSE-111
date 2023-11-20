#medium3
s=input("Enter word: ")
for i in range(0,len(s)):
    if s[i]==s[i].upper():
        x=i
        break
    else:
        continue
c=""
for i in range(x+1,len(s)):
    if s[i]!=s[i].upper():
        c+=s[i]
    else:
        break
if c=="":
    print("BLANK")
else:
    print(c)
    
    
    
        
