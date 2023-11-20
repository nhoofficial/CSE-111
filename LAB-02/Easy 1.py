x=int(input("Enter number1: "))
y=int(input("Enter number2: "))
def div(x,y):
    if x==0 or y==0:
        a=0
    else:
        a=(x/y)-y
    return a

print(div(x,y))
 
