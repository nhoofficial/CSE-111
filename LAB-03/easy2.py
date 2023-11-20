#easy2
s=input("Enter word: ")
s=s.replace(" ","")
c=""
for i in range(len(s)-1,-1,-1):
    c=c+s[i]
if s==c:
    print("True")
else:
    print("False")
    
    