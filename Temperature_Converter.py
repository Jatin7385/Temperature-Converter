def options():
    print("Which conversion would you like me to do?")
    print("1)Celcius to Farenheit")
    print("2)Celcius to Kelvin")
    print("3)Farenheit to Celcius")
    print("4)Farenheit to Kelvin")
    print("5)Kelvin to Celcius")
    print("6)Kelvin to Farenheit")
    print("7)Quit Program")
    choice = int(input("Enter your choice"))
    return choice

def accept():
    temperature=input("Enter the temperature")
    return temperature
#FORMULAS:F-32/9=C/5;K=C+273.15;F-32/9=K-273.15/5
def one(temp):
    F=((9*temp)/5)+32
    return F
def two(temp):
    K=temp+273.15
    return K
def three(temp):
    C=5*((temp-32)/9)
    return C
def four(temp):
    C=5*((temp-32)/9)
    K=C+273.15
    return K
def five(temp):
    C=temp-273.15
    return C
def six(temp):
    C=temp-273.15
    F=((9*C)/5)+32
    return F
choice=0
while choice!=7:
    choice=int(options())
    if choice==7:
        quit()
    temp=float(accept())
    if choice==1:
        F=one(float(temp))
        print(f"The converted temperature is {F} Farenheit")
    elif choice==2:
        K=two(float(temp))
        print(f"The converted temperature is {K} Kelvin")
    elif choice==3:
        C=three(float(temp))
        print(f"The converted temperature is {C} degree Celcius")
    elif choice==4:
        K=four(float(temp))
        print(f"The converted temperature is {K} Kelvin")
    elif choice==5:
        C=five(float(temp))
        print(f"The converted temperature is {C} degree Celcius")
    elif choice==6:
        F=six(float(temp))
        print(f"The converted temperature is {F} Farenheit")
    elif choice==7:
        quit()
    else:
        print("Wrong input")
        quit()


