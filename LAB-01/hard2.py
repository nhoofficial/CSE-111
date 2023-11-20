#hard2
row=int(input("Enter row"))
for i in range(row+1):
    for space in range(0,row-i,1):
        print(' ',end="")
    for j in range(1,2*i,1):
        if i==0 or j==1 or i==row or j==(2*i)-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()    
for i in range(row-1,-1,-1):
    for space in range(0,row-i,1):
        print(' ',end="")
    for j in range(1,2*i,1):
        if i==0 or j==1 or i==row or j==(2*i)-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()    
