#hard1
s1=input()
s1=s1.lower()
s1=sorted(s1)
s2=input()
s2=s2.lower()
s2=sorted(s2)
a={}
b={}
for i in range(len(s1)):
    a[i]=s1[i]
for i in range(len(s2)):
    b[i]=s2[i]
if len(a)==len(b):
    c=0
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
        else:
            print('Not anagram')
            break
        if c==len(s1):
            print('Those strings are anagram')
else:
    print('Those strings are not anagram')
        
    