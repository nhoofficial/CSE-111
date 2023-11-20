#Hard3
s=input("Enter word: ")
sc=0
uc=0
n=0
sp_chr=["@","_","#","$"]
num=["0","1","2","3","4","5","6","7","8","9"]
a=0
for i in range(0,len(s)):
    if s[i]==s[i].lower():
        sc+=1
    if s[i]==s[i].upper():
        uc+=1
    if s[i] in num:
        n+=1
    if s[i] in sp_chr:
        a+=1
if sc!=0 and uc!=0 and n!=0 and a!=0:
    print("OK")
else:
    if sc==0:
        print("Lower case missing",end=" ")
    if uc==0:
        print("Upper case missing",end=" ")
    if n==0:
        print("Digit missing",end=" ")
    if sc==0:
        print("Special case missing",end=" ")    
    
