#easy3
list=[]
for i in range(10):
    n=int(input("Enter number: "))
    if n in list:
        print("Enter different number")
        i-=1
    else:
        list.append(n)
