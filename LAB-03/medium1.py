#medium1
s=input("Enter word: ")
a=0
b=0
for i in range(0,len(s)):
    if s[i]==s[i].upper():
        a+=1
    else:
        b+=1
if a>b:
   print(s.upper())
else:
    print(s.lower())
    


