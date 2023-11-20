#easy1
a=input().split(',')
dict={}
for i in a:
    x=i.split(':')
    dict[x[0]]=int(x[1])
while True:
    n=input().upper()
    if n=="STOP":
        break
    else:
        n=int(n)
        if n in dict.values():
            print('True')
        else:
            print('False')
        
    


