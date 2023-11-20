#4
class Cat:
    def __init__(self,color=None,action=None):
        self.color=color
        self.action=action
    def printCat(self):
        if self.color==None and self.action==None:
            self.color="White"
            self.action='sitting'
            print("{} cat is {}".format(self.color,self.action)) 
        elif self.color!=None and self.action!=None:
            print("{} cat is {}".format(self.color,self.action)) 
        elif self.action==None:
            self.action='sitting'
            print("{} cat is {}".format(self.color,self.action)) 
            
    def changeColor(self,color):
        self.color=color
        
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()        
        

