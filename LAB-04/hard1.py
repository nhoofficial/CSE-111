#hard1
while True:
    abc = input("Enter number: ")
    if abc == "STOP":
        break
    else:
        a = True
        new = abc.split()
        n = len(new)
        b = []
        for i in range(n):
            t = int(new[i])
            b.append(t)
        lst = []
        for i in range(n-1):
            abc = abs(b[i+1]- b[i])
            lst.append(abc)
        lst.sort()
        for i in range(n-1):
            if lst[i] != i+1:
                a = False
        if a == False:
            print("Not UB Jumper")
        else:
            print("UB Jumper")


