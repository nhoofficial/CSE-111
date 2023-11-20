#3
class Wadiya():
    
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True
wadiya=Wadiya()
a=wadiya.name
print("Name of the president:",wadiya.name)
print("Designation:",wadiya.designation)
print("The number of wife:",wadiya.num_of_wife)
print("Is he/she a doctor:",wadiya.dictator)
wadiya.name="Donald Trump"
wadiya.designation="President"
wadiya.num_of_wife=1
wadiya.dictator=False
print("Name of the president:",wadiya.name)
print("Designation:",wadiya.designation)
print("The number of wife:",wadiya.num_of_wife)
print("Is he/she a doctor:",wadiya.dictator)
if wadiya.name!=a:
    print("Previous information lost.")
else:
    print("No, changing had no effect on previous value.")
    
    

    
    
    


