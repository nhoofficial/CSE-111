#easy3
s=input("Enter word: ")
if len(s)<4:
    print(s)
else:
    if s[len(s)-1]=="l" and s[len(s)-2]=="u" and s[len(s)-3]=="f":
        print(s+"ly")
    else:
        print(s+"ful")
    


