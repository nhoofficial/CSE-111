#easy1
s=input("Enter word: ")
s=s.lower()
c=0
a=""
for i in range(0,len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        c+=1
    else:
        a=a+s[i]
   
print(a,end="")
print(c)

