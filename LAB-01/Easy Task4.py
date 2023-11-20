num=int(input("Enter number"))
i=1
divc=0
while i<=num:
    if num%i==0:
        divc+=1
    i+=1
if divc==2:
    print("Prime number")
else:
    print("Not prime number")
    
    
    