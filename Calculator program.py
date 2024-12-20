a = int(input("Enter the first number: "))
x = input("Enter an oprator (+,-,*,/): ")
b = int(input("Enter the second number: "))

if x == "+":
    result = a + b
elif x == "-":
    result = a - b 
elif x == "*":
    result = a * b
elif x == "/":
    result = a / b
else:
    print(f"{x} is not valid operator")    

print("Result:", result)                  