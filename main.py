# Basic Calculator
# Author = Md Raahim Anowar

Operation = int(input("Choose your desired operation \n1. Addition '+' \n2. Subtraction '-' \n3. Multiplication '*' \n4. Exponential '**' \n5. Division '/' \n6. Modulus '%' \n7. Floor Division '//' "))
X = int(input("Enter the first number:"))
Y = int(input("Enter the second number:"))
if Operation ==1:
    add = X + Y
    print("Addititon is:",add)
elif Operation ==2:
    sub = X - Y
    print("Subtraction is:",sub)
elif Operation ==3:
    mult = X * Y
    print("Multiplication is:",mult)
elif Operation ==4:
    expo = X ** Y
    print("Exponential is:",expo)
elif Operation ==5:
    div = X / Y
    print("Division is:",div)
elif Operation ==6:
    mod = X % Y
    print("Modulus is:",mod)
elif Operation ==7:
    fdiv = X // Y
    print("Floor Division is:",fdiv)
else:
    print("Enter a vlid option")