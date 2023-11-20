
#hard1
s1=input("Enter string1: ")
s2=input("Enter string2: ")
c=""
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s2[j]==s1[i]:
            c+=s2[j]
if c=="":
    print("Nothing in common")
else:
    print(c)
    
            
            