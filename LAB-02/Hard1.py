#hard1
name=input("Enter name: ")
salary=int(input("Enter salary: "))
yyyy=int(input("Enter year: "))
mm=int(input("Enter month: "))
dd=int(input("Enter day: "))
import datetime
x = (datetime.date(yyyy,mm,dd))

def bonus(name,salary,x):
    if 2020-yyyy<5:
        p=salary*(10/100)
        print(name,":",p)
    elif 2020-yyyy<=10:
        p=salary*(10/100)+5000
        print(name,":",p)
    elif 2020-yyyy>10:
        p=salary*(15/100)+15000
        print(name,":",p)
bonus(name,salary,x)        
        
        
