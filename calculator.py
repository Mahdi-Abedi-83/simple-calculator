def hesab(x, y, z):
    if x.isdigit() != True or z.isdigit() != True:
        print("Something went wrong!")
    if y != "+" and y != "-" and y != "*" and y != "/":
        print("The operator is not valid!")
    else:
            x = int(x)
            z = int(z)
            if y == "*":
                print(x * z)
        
            if y == "/":
                print(x / z)
        
            if y == "+":
                print(x + z)
        
            if y == "-":
                print(x - z)


x = (input("enter number1 = "))
y = input("enter function (* / + -) = ")
z = (input("enter number2 = "))
hesab(x, y, z)
        
