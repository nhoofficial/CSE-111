num=int(input("Enter number"))
c=0
while num>0:
    if num%2!=0:
        c+=1
    num=num//2  
sum=0
for i in range(c):
    sum=sum+2**i
print(sum)
