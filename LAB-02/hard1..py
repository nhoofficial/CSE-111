# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:56:52 2020

@author: TUHIN
"""


#hard1
cm=int(input("Enter current month: "))
cd=int(input("Enter current date: "))
name=input("Enter name: ")
salary=int(input("Enter salary: "))
yyyy=int(input("Enter year: "))
mm=int(input("Enter month: "))
dd=int(input("Enter day: "))
if cm>mm or dd<cd:
    yyyy-=1
import datetime
x = (datetime.date(yyyy,mm,dd))

def bonus(*args):
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