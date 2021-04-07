print("Enter 3 numbers")
num1 = input()
num2 = input()
num3 = input()

if(int(num1)> int(num2)):
    if(int(num1)> int(num3)):
        print(num1 + " is greatest")
    else :
        print(num3 + "is greatest")
else:
    if(int(num2)> int(num3)):
        print(num2 + " is greatest")
    else:
        print(num3 +" is greatest")