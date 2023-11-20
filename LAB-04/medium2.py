#med2
#med2
n=int(input("Enter number: "))
num=[]
lst=[]
x=[]
for i in range(n):
    num1,num2,num3=(input().split())
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    sum=num1+num2+num3
    num.append(num1)
    num.append(num2)
    num.append(num3)
    lst.append(sum)
print(max(lst))
for i in range(0,len(num),3):
    sum1=num[i]+num[i+1]+num[i+2]
    if sum1==max(lst):
        x.append(num[i])
        x.append(num[i+1])
        x.append(num[i+2])
print(x)        
    


