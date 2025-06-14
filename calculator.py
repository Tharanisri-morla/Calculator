operator = input("Enter a operator(+,-,%,/,*):")
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
if operator == "+":
    result=num1+num2
    print(f"The addition of the {num1}and {num2} is (round{result}) " )
elif operator == "-":
    result=num1-num2
    print(f"The subtraction of the {num1}and {num2} is (round {result} )  " )
elif operator == "%":
    result=num1%num2
    print(f"The modulo division of the {num1}and {num2} is (round{result}) ")
elif operator == "/":
    result=num1/num2
    print(f"The division of the {num1}and {num2} is (round {result} )" )
elif operator == "*":
    result=num1*num2
    print(f"The multiplication of the {num1}and {num2} is (round {result})  " )
else:
    print(" The given operator is not valid it's out of syllobus")

