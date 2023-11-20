#hard2
n=int(input("Enter n"))
def year(n):
    y=n//365
    n=n%365
    m=n//30
    n=n%30
    print(y,"years",",",m,"month","and",n,"days")
year(n)    