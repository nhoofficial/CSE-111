#medium2
s=input()
d={}
while s!='STOP':
    num=int(s)
    if num in d:
        d[num]+=1
    else:
        d[num]=1
    s=input()  
for i in d:
    print(i,'-',d[i],'times')
    
    
                                                    