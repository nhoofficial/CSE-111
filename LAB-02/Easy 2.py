#Easy task2
height=int(input("Enter height: "))
kg=int(input("Enter weight: "))
def BMI(height,kg):
    m=height/100
    BMI=kg/(m*m)
    if BMI<18.5:
        print("Your score is",BMI,end="")
        print("You are underweight")
    elif BMI<=24.9:
        print("Your score is",BMI,end="")
        print("You are normal")
    elif BMI<=30:
        print("Your score is",BMI,end="")
        print("You are overweight")
    else:
        print("Your score is",BMI,end="")
        print("You are obese")

BMI(height,kg)
        
        
        

        



    
    

