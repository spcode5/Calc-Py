# calculator 
def sum(a, b): #function to add two numbers
    return (a+b)
a = int(input("Enter 1st number:"))
#accept an integer input from user
b = int(input("Enter 2nd number:"))

print(f'sum of {a} and {b} is {sum(a, b)}')
def add(x, y):#addition function
    return x + y 
def suntract(x, y): #subtraction function
    return x - y
def multiply(x, y): #multiplication function
    return x * y
def divide(x, y): #division funtion
    if y !=0:
        return x / y
    else:
        return "error! division by zero not possible"
    Print("Select operation.")
    print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = input("enter choice(1/2/3/4):")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
if choice == '1':
    print(f'{num1}+{num2}={add(num1,num2)}')
elif choice == '2':
    print(f'{num1}-{num2}={suntract(num1,num2)}')
elif choice == '3':
    print(f'{num1}*{num2}={multiply(num1,num2)}')
elif choice == '4':
    print(f'{num1}/{num2}={divide(num1,num2)}')
else:
    print("Invalid input")
        



    
                               