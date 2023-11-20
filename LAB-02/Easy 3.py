#easy3
x=int(input("Enter x"))
y=int(input("Enter y"))
z=int(input("Enter z"))
def div(x,y,z):
    sum=0
    i=x
    while i<y:
        sum+=i
        i+=z
    print(sum)

div(x,y,z)    
            
        
