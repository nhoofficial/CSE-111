#2
class Customer:
    print("Hello!")
    def __init__(self,name):
        self.name=name
    def greet(self,x=None):
        print(self.name,end=',')
        self.x=x
    def purchase(self,*args):
        print("you purchased",len(args),'item(s):')
        for i in args:
            print(i)
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")            
        