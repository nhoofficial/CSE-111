a=input("Enter name: ")
def x(a):
    a=a.lower()
    a=a.replace(" ","")
    new=""
    for i in range(len(a)-1,-1,-1):
        new=new+a[i]
    if a==new:
        print("Palindrome")
    else:
        print("Not a palindrome")
x(a)        
        
    
      