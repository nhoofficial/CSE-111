#easy3
a={}
for i in range(10):
    n=int(input("Enter number: "))
    if n in a.values():
        print("Enter different number")
        i-=1
    else:
        a.update({i:n})
    

