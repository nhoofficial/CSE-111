#hard2
s=input("Enter string: ")
sc=[]
uc=[]
n=[]
for i in range(0,len(s)):
    if s[i]==s[i].lower():
        sc.append(s[i])
    else:
        if s[i]==s[i].upper():
            uc.append(s[i])
sc.sort()
print(sc)
print(uc)

            
        
        
