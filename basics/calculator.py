first = float(input("enter first number : "))
second = float(input("enter second number : "))
operation = input("enter operation you want to perform (sum, subtract, multiply, divide, power) : ")
sum = first + second
subtract = first - second
multiply = first * second
divide = first / second
power = first ** second

if operation=='sum' : 
    print(sum)

elif operation=='subtract' : 
    print(subtract)

elif operation=='multiply' :
    print(multiply)

elif operation=='divide' :
    print(divide)

elif operation=='power' :
    print(power)

else :
    print("enter valid operation!")
