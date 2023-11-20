#hard2
s=input("Enter string: ")
a=""
b=""
c=""
odd=""
even=""
for i in range(len(s)):
    if s[i].isupper():
        a+=s[i]
    if s[i].islower():
        b+=s[i]
    if s[i].isnumeric():
        c+=s[i]
a=list(a)        
a.sort()
x=''.join(a)


b=list(b)
b.sort()
y=''.join(b)


for i in c:
    a=int(i)
    if a%2==0:
        even+=i
    else:
        odd+=i
print(y,end="")
print(x,end="")
print(odd,end="")
print(even,end="")


        
        
        



