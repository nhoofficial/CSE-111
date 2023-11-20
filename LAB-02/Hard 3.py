#hard3
s=input("Enter paragraph: ")
def cap(s):
    n=list(s)
    for i in range(0,len(s)):
        if i==0:
            n[i]=n[i].upper()
        if i>=2:
            if n[i-2]=="." or n[i-2]=="!" or n[i-2]=="?":
                n[i]=n[i].upper()
        if n[i-1]==" " and n[i]=="i" and n[i+1]==" ":
            n[i]=n[i].upper()
    c=""
    for j in range(0,len(n)):
        c=c+n[j]
    print(c)
cap(s)    