#medium2
s=input("Enter word: ")
num=["0","1","2","3","4","5","6","7","8","9"]
try:
    i=int(s)
    print("NUMBER")
except:
    s=s.lower()
    for i in s:
        if i in num:
            print("MIXED")
            break
    else:
        print("WORD")
               
        

