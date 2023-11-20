#medium4
n=int(input("Enter number: "))
s=input("Enter String: ")
s=s.split(",")
list=[]
for i in range(0,len(s),3):
    list.append(s[i])
print(list)    


