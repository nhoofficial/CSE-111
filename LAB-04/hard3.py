#hard3
n=int(input("Enter number: "))
k=int(input("Enter number: "))
a=list=(int(x) for x in input().split(" "))
b=0
for i in a:
    if (5-i)>=k:
        b+=1
b=b/3
print(int(b))

