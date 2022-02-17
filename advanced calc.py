num1 = float(input("Enter a number: "))
op = input("Enter a operator : ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(int(num1+num2))

elif op == "-":
    print(int(num1-num2))

elif op == "/":
    print(int(num1/num2))

elif op == "*":
    print(int(num1*num2))

else:
    print("Invalid operator")

