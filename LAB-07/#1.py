#1
first_value=int(input("Enter number 1: "))
operator=input("Enter operator: ")
second_value=int(input("Enter number 2: "))
class Calculator:
    def __init__(self,first_value,operator,second_value):
        self.first_value=first_value
        self.operator=operator
        self.second_value=second_value
    print('Lets calculate')    
    def add(self):
        print('Value 1:',self.first_value)
        print('Operator:',self.operator)
        print('Value 2:',self.second_value)
        print('Result:',self.first_value+self.second_value)
    def substract(self):
        print('Value 1:',self.first_value)
        print('Operator:',self.operator)
        print('Value 2:',self.second_value)
        print('Result:',self.first_value-self.second_value)
    def multiply(self):
        print('Value 1:',self.first_value)
        print('Operator:',self.operator)
        print('Value 2:',self.second_value)
        print('Result:',self.first_value*self.second_value)
    def divide(self):
        print('Value 1:',self.first_value)
        print('Operator:',self.operator)
        print('Value 2:',self.second_value)
        print('Result:',self.first_value/self.second_value)   
c1=Calculator(first_value,operator,second_value)
if c1.operator=="+":
    c1.add()
elif c1.operator=='-':
    c1.substract()
elif c1.operator=='*':
    c1.multiply()
else:
    c1.divide()
    
    
    
    
    
        


            
    
        