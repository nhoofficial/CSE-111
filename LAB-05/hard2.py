#HARD2
a={0:" ",1:".,?!:",2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}
s=input().upper()
c=""
for i in s:
    for x,y in a.items():
        if i in y:
            idx=y.index(i)+1
            c+=str(x)*idx
print(c)       

