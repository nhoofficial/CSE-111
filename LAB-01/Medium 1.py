num=int(input("Enter number"))
first=0
second=1
sum=first+second
print(first,end=" ")
print(second,end=" ")
print(sum,end=" ")
while sum<num:
    print(sum,end=" ")
    first=second
    second=sum
    sum=first+second



