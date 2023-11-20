#medium1
n=[]
while True:
    x=input("Enter number: ")
    if x =="STOP":
        break
    
    else:
        n.append(int(x))
c=0        
for i in n:
    if n.index(i)==c:
        print(i,"-",n.count(i),"times")
        c+=1
       