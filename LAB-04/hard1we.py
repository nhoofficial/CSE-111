#hard1
while True:
    s=input("Enter number: ")
    if s=="STOP":
        break
    else:
        s=s.split()
        a=[]
        lst=[]
        for i in range(len(s)):
            a.append(int(s[i]))
        b=len(a)
        for i in range(b):
            if a[i+1]-a[i]<b:
                lst.append(a[i])
        if len(lst)==b:
            print("UB Jumper")
        else:
            print("Not UB Jumper")
