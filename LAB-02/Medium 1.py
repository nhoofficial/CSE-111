#med1
burger=input("Enter name: ")
burger.lower()
burger.replace(" ","")
location=input("Enter location: ")
location.lower()
location.replace(" ","")
def cost(burger,location):
    if burger=="bbq chicken cheese burger":
        if location=="mohakhali":
            cost=250+250*8/100+40
            print(cost)
        else:
            cost=250+250*8/100+60
            print(cost)
    elif burger=="beef burger":
        if location=="mohakhali":
            cost=170+170*8/100+40
            print(cost)
        else:
             cost=170+170*8/100+60
             print(cost)
    else:
        if location=="mohakhali":
            cost=200+200*8/100+40
            print(cost)
        else:
            cost=200+200*8/100+60
            print(cost)
cost(burger,location)     
    