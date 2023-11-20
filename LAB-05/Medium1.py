#medium1
a={}
a1=list(input().split(','))
for i in a1:
    x=i.split(':')
    a[x[0]]=int(x[1])    
b={}
b1=list(input().split(','))
for i in b1:
    x=i.split(':')
    b[x[0]]=int(x[1])  


for key in b:
    if key in a:
        b[key]=b[key]+a[key] #a:100,b:100,c:200,d:300
dic={**a,**b}   #a:100,b:100,d:200,e:300

x=[]  
for i in dic.values():
    if i not in x:
        x.append(i)
x.sort()
x=tuple(x)
print("Values:",x)
    
        
    
    
    


